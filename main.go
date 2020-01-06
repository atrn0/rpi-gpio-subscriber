package main

import (
	"cloud.google.com/go/pubsub"
	"context"
	"log"
)

const (
	topicName = "hello_topic"
	subName   = "sub_one"
)

func main() {
	ctx := context.Background()

	client, err := pubsub.NewClient(ctx, "project-id")
	if err != nil {
		log.Fatalln(err)
	}

	topic, err := client.CreateTopic(ctx, topicName)
	if err != nil {
		log.Fatalln(err)
	}

	subConfig := pubsub.SubscriptionConfig{Topic: topic}
	sub, err := client.CreateSubscription(ctx, subName, subConfig)
	if err != nil {
		log.Fatalln(err)
	}

	err = sub.Receive(ctx, func(ctx context.Context, m *pubsub.Message) {
		log.Printf("Got message: %s", m.Data)
		m.Ack()
	})
	if err != nil {
		log.Fatalln(err)
	}

	err = client.Close()
	if err != nil {
		log.Fatalln(err)
	}

	topic.Stop()
}
