package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"os/signal"

	"github.com/isard-vdi/isard/disk-operations/cfg"
	"github.com/isard-vdi/isard/disk-operations/diskoperations"
	"github.com/isard-vdi/isard/disk-operations/env"
	"github.com/isard-vdi/isard/disk-operations/transport/grpc"
	"go.uber.org/zap"
)

func main() {
	logger, err := zap.NewProduction()
	if err != nil {
		log.Fatalf("create logger: %v", err)
	}
	defer logger.Sync()
	sugar := logger.Sugar()

	env := &env.Env{
		Sugar: sugar,
		Cfg:   cfg.Init(sugar),
	}

	env.DiskOperations = diskoperations.New(env)

	ctx, cancel := context.WithCancel(context.Background())

	go grpc.Serve(ctx, env)
	env.WG.Add(1)

	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt)

	select {
	case <-stop:
		fmt.Println("")
		env.Sugar.Info("stoping disk-operations...")

		cancel()

		env.WG.Wait()
	}
}
