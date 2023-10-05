docker exec -it schema-registry kafka-avro-console-consumer \
  --bootstrap-server broker:29092 \
  --topic pg-person \
  --from-beginning \
  --property schema.registry.url=http://schema-registry:8081 \
  --property print.key=true \
  --property key.separator=" | "