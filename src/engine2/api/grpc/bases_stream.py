import grpc
from engine.grpc.proto import bases_stream_pb2
from engine.grpc.proto import bases_stream_pb2_grpc

import rethinkdb as r
from rethinkdb.errors import (
    ReqlAuthError,
    ReqlCursorEmpty,
    ReqlDriverError,
    ReqlError,
    ReqlInternalError,
    ReqlNonExistenceError,
    ReqlOpFailedError,
    ReqlOpIndeterminateError,
    ReqlPermissionError,
    ReqlQueryLogicError,
    ReqlResourceLimitError,
    ReqlRuntimeError,
    ReqlServerCompileError,
    ReqlTimeoutError,
    ReqlUserError)
from engine.grpc.lib.database import rdb

from engine.grpc.statemachines.base_sm import BaseSM, StateInvalidError
 
class BasesStreamServicer(bases_stream_pb2_grpc.BasesStreamServicer):
    """
    gRPC server for Bases Changes stream Service
    """
    def __init__(self, app):
        self.base_sm = BaseSM()
        
    def Changes(self, request_iterator, context):
        try:
            with rdb() as conn:
                for c in r.table('domains').get_all(r.match('template'), index='kind').pluck('id','status','detail').changes().run(conn):
                    ''' DELETED '''
                    if c['new_val'] is None:
                        yield bases_stream_pb2.BasesStreamResponse( desktop_id=c['old_val']['id'],
                                                                        state='DELETED',
                                                                        detail=c['old_val']['detail'],
                                                                        next_actions=[])
                        continue
                    ''' NEW '''
                    if c['old_val'] is None:
                        yield bases_stream_pb2.BasesStreamResponse( desktop_id=c['new_val']['id'],
                                                                        state='NEW',
                                                                        detail=c['new_val']['detail'],
                                                                        next_actions=[])
                        continue
                    
                    ''' Is it a valid state? '''
                    if c['new_val']['status'].upper() not in self.bases_sm.get_states(): continue
                    
                    ''' Is it a detail update? '''
                    if c['old_val']['status'] == c['new_val']['status']: continue
                    
                    new_state=c['new_val']['status'].upper()
                    yield bases_stream_pb2.BasesStreamResponse( desktop_id=c['new_val']['id'],
                                                                    state=new_state,
                                                                    detail=c['new_val']['detail'],
                                                                    next_actions=self.bases_sm.get_next_actions(new_state))  
        except StateInvalidError:
            context.set_details('State invalid: ')
            context.set_code(grpc.StatusCode.INTERNAL)               
            return bases_stream_pb2.BasesStreamResponse()  
        except Exception as e:
            print(e)
            context.set_details('Unable to access database.')
            context.set_code(grpc.StatusCode.INTERNAL)               
            return bases_stream_pb2.BasesStreamResponse()  