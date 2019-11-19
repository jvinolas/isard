# ~ import sqlalchemy as sa
# ~ from sqlalchemy.orm import relationship, backref
# ~ from sqlalchemy.inspection import inspect as _inspect
# ~ from sqlalchemy.ext.orderinglist import ordering_list

from models import db, Base
from models.base_mixin import BaseMixin

from models.domain import Domain

# ~ from models.parser.xml_parser import XmlParser

# ~ def same_as(column_name):
    # ~ def default_function(context):
        # ~ return context.current_parameters.get(column_name)
    # ~ return default_function
    
# ~ class Domain_Sound(BaseMixin, Base):
    # ~ __tablename__ = 'domain_sound'

    # ~ __table_args__ = (
            # ~ sa.UniqueConstraint("domain_id", "sound_id"),
        # ~ )
        
    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), primary_key=True)
    # ~ sound_id = sa.Column(sa.Integer, sa.ForeignKey('sound_xml.id'), primary_key=True)
    
    # ~ sound = relationship("SoundXML", back_populates="domain")
    # ~ domain = relationship("Domain", back_populates="sound")

# ~ class Domain_Cpu(BaseMixin, Base):
    # ~ __tablename__ = 'domain_cpu'
        
    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), primary_key=True)
    # ~ cpu_id = sa.Column(sa.Integer, sa.ForeignKey('cpu_xml.id')) #, primary_key=True)
    # ~ match = sa.Column(sa.String, default='exact')
    # ~ fallback = sa.Column(sa.String, default='allow')
    # ~ model = sa.Column(sa.String, default='Haswell-noTSX')
    # ~ check = sa.Column(sa.String, default='partial')
    
    # ~ cpu = relationship("CpuXML", back_populates="domain")
    # ~ domain = relationship("Domain", back_populates="cpu")
            
# ~ class Domain_Vcpu(BaseMixin, Base):
    # ~ __tablename__ = 'domain_vcpu'
        
    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), primary_key=True)
    # ~ vcpu_id = sa.Column(sa.Integer, sa.ForeignKey('vcpu_xml.id')) #, primary_key=True)
    # ~ vcpus = sa.Column(sa.Integer, nullable=False)
    
    # ~ vcpu = relationship("VcpuXML", back_populates="domain")
    # ~ domain = relationship("Domain", back_populates="vcpu")
    
# ~ class Domain_Memory(BaseMixin, Base):
    # ~ __tablename__ = 'domain_memory'
        
    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), primary_key=True)
    # ~ memory_id = sa.Column(sa.Integer, sa.ForeignKey('memory_xml.id')) #, primary_key=True)
    # ~ unit = sa.Column(sa.String, default='MiB')
    # ~ mem = sa.Column(sa.Integer, nullable=False)
    # ~ maxmemory = sa.Column(sa.Integer, default=same_as('mem'))
    # ~ currentmemory = sa.Column(sa.Integer, default=same_as('mem'))
    
    # ~ memory = relationship("MemoryXML", back_populates="domain")
    # ~ domain = relationship("Domain", back_populates="memory")
            
# ~ class Domain_Media(BaseMixin, Base):
    # ~ __tablename__ = 'domain_media'

    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), primary_key=True)
    # ~ media_id = sa.Column(sa.Integer, sa.ForeignKey('media_xml.id'), primary_key=True)
    # ~ ppath = sa.Column(sa.String, default="disks/")
    # ~ rpath = sa.Column(sa.String, default="domains/")
    # ~ filename = sa.Column(sa.String, nullable=False)
    # ~ bus = sa.Column(sa.String, default="ide")
    # ~ format = sa.Column(sa.String, default="raw")
    # ~ order = sa.Column(sa.Integer, nullable=False)
    
    # ~ medias = relationship("MediaXML", back_populates="domains")
    # ~ domain = relationship("Domain", back_populates="medias")

# ~ class Domain_Interface(BaseMixin, Base):
    # ~ __tablename__ = 'domain_interface'

    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), primary_key=True)
    # ~ interface_id = sa.Column(sa.Integer, sa.ForeignKey('interface_xml.id'), primary_key=True)
    # ~ order = sa.Column(sa.Integer, nullable=False)
    # ~ source = sa.Column(sa.String, default='default')
    # ~ model = sa.Column(sa.String, default='virtio')
    # ~ mac = sa.Column(sa.String)
    
    # ~ interfaces = relationship("InterfaceXML", back_populates="domains")
    # ~ domains = relationship("Domain", back_populates="interfaces")

# ~ class Domain_Graphic(BaseMixin, Base):
    # ~ __tablename__ = 'domain_graphic'

    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), primary_key=True)
    # ~ graphic_id = sa.Column(sa.Integer, sa.ForeignKey('graphic_xml.id'), primary_key=True)
    # ~ order = sa.Column(sa.Integer, nullable=False)
    
    # ~ graphic = relationship("GraphicXML", back_populates="domain")
    # ~ domain = relationship("Domain", back_populates="graphic")
        
# ~ class Domain_Video(BaseMixin, Base):
    # ~ __tablename__ = 'domain_video'

    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), primary_key=True)
    # ~ video_id = sa.Column(sa.Integer, sa.ForeignKey('video_xml.id'), primary_key=True)
    # ~ order = sa.Column(sa.Integer, nullable=False)
    
    # ~ videos = relationship("VideoXML", back_populates="domains")
    # ~ domain = relationship("Domain", back_populates="videos")
      
class Desktop(Domain):
    __mapper_args__ = {
        'polymorphic_identity':'manager'
    }
    
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True)
    # ~ state = sa.Column(sa.String, default='STATE_UNKNOWN')
    
    # ~ domain_xml_id = sa.Column(sa.Integer, sa.ForeignKey('domain_xml.id'), nullable=False)
    # ~ domain_xml = relationship("DomainXML")  
    # ~ boot = relationship("Boot", order_by="Boot.order",
                            # ~ collection_class=ordering_list('order'),
                            # ~ cascade="all, delete-orphan")
                                
    # ~ disk = relationship('Disk')
    # ~ medias = relationship("Domain_Media", 
                                        # ~ back_populates="domain")
    # ~ graphic = relationship("Domain_Graphic", 
                                        # ~ back_populates="domain")
    # ~ interfaces = relationship("Domain_Interface", 
                                        # ~ back_populates="domains")                                                                                                                                                                                                                                                
    # ~ videos = relationship("Domain_Video", 
                                        # ~ back_populates="domain") 
    # ~ memory = relationship("Domain_Memory", 
                                        # ~ back_populates="domain") 
    # ~ vcpu = relationship("Domain_Vcpu", 
                                        # ~ back_populates="domain")                                         
    # ~ cpu = relationship("Domain_Cpu", 
                                        # ~ back_populates="domain")   
                                        
    # ~ sound = relationship("Domain_Sound", 
                                        # ~ back_populates="domain")  
                                                                                
    # ~ memory = relationship('MemoryXML')
    # ~ vcpu = relationship('VcpuXML')
    # ~ vcpu = sa.Column(sa.Integer)
    # ~ memory = sa.Column(sa.Integer)

        
    # ~ def get_xml(domain_name):
        # ~ try:
            # ~ domain = Domain.by_name(domain_name)
            # ~ domain_tree = XmlParser(db.query(DomainXML).filter(DomainXML.id == domain.domain_xml_id).first().xml)
            # ~ domain_tree.domain_name_update(domain.name)
            # ~ domain_tree.domain_memory_update(MemoryXML.get_domain_memory(domain.id))
            # ~ domain_tree.domain_vcpu_update(VcpuXML.get_domain_vcpu(domain.id))
            # ~ domain_tree.domain_cpu_update(CpuXML.get_domain_cpu(domain.id))
            # ~ domain_tree.domain_boot_update([boot.name for boot in Boot.list(domain.name)])
            # ~ domain_tree.domain_sound_add(SoundXML.get_domain_sound(domain.id))
            # ~ for disk in Disk.get_domain_disks(domain.id):
                # ~ domain_tree.domain_disk_add(disk)
            # ~ for media in MediaXML.get_domain_medias(domain.id):
                # ~ domain_tree.domain_disk_add(media)
            # ~ for interface in InterfaceXML.get_domain_interfaces(domain.id):
                # ~ domain_tree.domain_interface_add(interface)         
            # ~ for graphic in GraphicXML.get_domain_graphics(domain.id):
                # ~ domain_tree.domain_graphic_add(graphic)  
            # ~ for video in VideoXML.get_domain_video(domain.id):
                # ~ domain_tree.domain_graphic_add(video) 
            # ~ return domain_tree.to_xml()

        # ~ except Exception as e:
            # ~ raise
        
# ~ class Disk(BaseMixin, Base):
    # ~ __tablename__ = 'disk'
    
    # ~ __table_args__ = (
            # ~ sa.UniqueConstraint("domain_id", "order"),
        # ~ )
    
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True)
    # ~ order = sa.Column(sa.Integer)
    
    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id')) 
    
    # ~ xml_id = sa.Column(sa.Integer, sa.ForeignKey('disk_xml.id'), nullable=False)  
    # ~ xml = relationship('DiskXML')
    
    # ~ ppath = sa.Column(sa.String, default="disks/")
    # ~ rpath = sa.Column(sa.String, default="domains/")
    # ~ filename = sa.Column(sa.String, nullable=False)
    
    # ~ bus = sa.Column(sa.String, default='virtio')
    # ~ size = sa.Column(sa.Integer, default=10)
    # ~ format = sa.Column(sa.String, default='qcow2') 

    # ~ def get_domain_disks(domain_id):
        # ~ disks = db.query(Disk).filter(Disk.id == domain_id).all()
        # ~ disks_list = []
        # ~ for disk in disks:
            # ~ disks_list.append({'name':disk.name,
                            # ~ 'xml': db.query(DiskXML).filter(DiskXML.id == disk.xml_id).first().xml,
                            # ~ 'ppath': disk.ppath,
                            # ~ 'rpath': disk.rpath,
                            # ~ 'filename': disk.filename,
                            # ~ 'bus': disk.bus,
                            # ~ 'size': disk.size,
                            # ~ 'format': disk.format,
                            # ~ 'order': disk.order})
        # ~ return disks_list

# ~ class SoundXML(BaseMixin, Base):
    # ~ __tablename__ = 'sound_xml'
    
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True)
    # ~ xml = sa.Column(sa.String, unique=True)

    # ~ domain = relationship("Domain_Sound", 
                                        # ~ back_populates="sound")      

    # ~ def get_domain_sound(domain_id):
        # ~ domain_sound = db.query(Domain_Sound).filter(Domain_Sound.domain_id == domain_id).first()
        # ~ if domain_sound == None: return False
        # ~ sound = db.query(SoundXML).filter(SoundXML.id == domain_sound.sound_id).first()
        # ~ return {**sound._as_dict(), **domain_sound._as_dict()}
        
# ~ class MemoryXML(BaseMixin, Base):
    # ~ __tablename__ = 'memory_xml'
    
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True)
    # ~ xml = sa.Column(sa.String, unique=True)

    # ~ domain = relationship("Domain_Memory", 
                                        # ~ back_populates="memory")      

    # ~ def get_domain_memory(domain_id):
        # ~ domain_memory = db.query(Domain_Memory).filter(Domain_Memory.domain_id == domain_id).first()
        # ~ memory = db.query(MemoryXML).filter(MemoryXML.id == domain_memory.memory_id).first()
        # ~ dict = {**memory._as_dict(), **domain_memory._as_dict()}
        # ~ dict['memory'] = dict.pop('mem')
        # ~ return dict
        
# ~ class CpuXML(BaseMixin, Base):
    # ~ __tablename__ = 'cpu_xml'
    
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True)
    # ~ xml = sa.Column(sa.String, unique=True)

    # ~ domain = relationship("Domain_Cpu", 
                                        # ~ back_populates="cpu")  

    # ~ def get_domain_cpu(domain_id):
        # ~ domain_cpu = db.query(Domain_Cpu).filter(Domain_Cpu.domain_id == domain_id).first()
        # ~ cpu = db.query(CpuXML).filter(CpuXML.id == domain_cpu.cpu_id).first()
        # ~ return {**cpu._as_dict(), **domain_cpu._as_dict()}
                        
# ~ class VcpuXML(BaseMixin, Base):
    # ~ __tablename__ = 'vcpu_xml'
    
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True)
    # ~ xml = sa.Column(sa.String, unique=True)

    # ~ domain = relationship("Domain_Vcpu", 
                                        # ~ back_populates="vcpu")   

    # ~ def get_domain_vcpu(domain_id):
        # ~ domain_vcpu = db.query(Domain_Vcpu).filter(Domain_Vcpu.domain_id == domain_id).first()
        # ~ vcpu = db.query(VcpuXML).filter(VcpuXML.id == domain_vcpu.vcpu_id).first()
        # ~ return {**vcpu._as_dict(), **domain_vcpu._as_dict()}
                        
# ~ class DiskXML(BaseMixin, Base):
    # ~ __tablename__ = "disk_xml"
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True, nullable=False)
    # ~ xml = sa.Column(sa.String, unique=True, nullable=False)

# ~ class DomainXML(BaseMixin, Base):
    # ~ __tablename__ = "domain_xml"
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True, nullable=False)
    # ~ xml = sa.Column(sa.String, unique=True, nullable=False)

# ~ class MediaXML(BaseMixin, Base):
    # ~ __tablename__ = "media_xml"
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True, nullable=False)
    # ~ xml = sa.Column(sa.String, unique=True, nullable=False)
    
    # ~ domains = relationship("Domain_Media", 
                                        # ~ back_populates="medias")      

    # ~ def get_domain_medias(domain_id):
        # ~ domain_medias = db.query(Domain_Media).filter(Domain_Media.domain_id == domain_id).all()
        # ~ medias_list = []
        # ~ for domain_media in domain_medias:
            # ~ media = db.query(MediaXML).filter(MediaXML.id == domain_media.media_id).first()
            # ~ medias_list.append({**media._as_dict(), **domain_media._as_dict()})
        # ~ return medias_list         

# ~ class GraphicXML(BaseMixin, Base):
    # ~ __tablename__ = "graphic_xml"
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True, nullable=False)
    # ~ xml = sa.Column(sa.String, unique=True, nullable=False)
    
    # ~ domain = relationship("Domain_Graphic", 
                                        # ~ back_populates="graphic")      

    # ~ def __init__(self, name, xml):
        # ~ self.name = name
        # ~ self.xml = xml

    # ~ def get_domain_graphics(domain_id):
        # ~ domain_graphics = db.query(Domain_Graphic).filter(Domain_Graphic.domain_id == domain_id).all()
        # ~ graphics_list = []
        # ~ for domain_graphic in domain_graphics:
            # ~ graphic = db.query(GraphicXML).filter(GraphicXML.id == domain_graphic.graphic_id).first()
            # ~ graphics_list.append({**graphic._as_dict(), **domain_graphic._as_dict()})
        # ~ return graphics_list    
        
# ~ class VideoXML(BaseMixin, Base):
    # ~ __tablename__ = "video_xml"
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True, nullable=False)
    # ~ xml = sa.Column(sa.String, unique=True, nullable=False)
    
    # ~ domains = relationship("Domain_Video", 
                                        # ~ back_populates="videos")      

    # ~ def get_domain_video(domain_id):
        # ~ domain_videos = db.query(Domain_Video).filter(Domain_Video.domain_id == domain_id).all()
        # ~ videos_list = []
        # ~ for domain_video in domain_videos:
            # ~ video = db.query(VideoXML).filter(VideoXML.id == domain_video.video_id).first()
            # ~ videos_list.append({**video._as_dict(), **domain_video._as_dict()})
        # ~ return videos_list  
        
# ~ class InterfaceXML(BaseMixin, Base):
    # ~ __tablename__ = "interface_xml"
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, unique=True, nullable=False)
    # ~ xml = sa.Column(sa.String, unique=True, nullable=False)
    
    # ~ domains = relationship("Domain_Interface", 
                                        # ~ back_populates="interfaces")      

    # ~ def get_domain_interfaces(domain_id):
        # ~ domain_interfaces = db.query(Domain_Interface).filter(Domain_Interface.domain_id == domain_id).all()
        # ~ interfaces_list = []
        # ~ for domain_interface in domain_interfaces:
            # ~ interface = db.query(InterfaceXML).filter(InterfaceXML.id == domain_interface.interface_id).first()
            # ~ interfaces_list.append({**interface._as_dict(), **domain_interface._as_dict()})
        # ~ return interfaces_list  

# ~ class Boot(BaseMixin, Base):
    # ~ __tablename__ = "boot"
    # ~ id = sa.Column(sa.Integer, primary_key=True)
    # ~ name = sa.Column(sa.String, nullable=False)
    # ~ domain_id = sa.Column(sa.Integer, sa.ForeignKey('domain.id'), nullable=False)
    # ~ order = sa.Column(sa.Integer, nullable=False)

    # ~ __table_args__ = (
            # ~ sa.UniqueConstraint(domain_id, name),
        # ~ )    
            
    # ~ def update(domain_name, boots):
        # ~ db.boot.remove(db.query(Boot).filter(Boot.domain_id == Domain.by_name(domain_name).id).delete())
        # ~ db.domain.boot.append([Boot(domain_id=Domain.by_name(domain_name).id, name=boot) for boot in boots]) 
        # ~ return True

    # ~ def list(domain_name):
        # ~ return db.query(Boot).filter(Boot.domain_id==Domain.by_name(domain_name).id).all()
