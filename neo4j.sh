docker run -d \
  --name neo4j \
  -p 7474:7474 \
  -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/neo4j12345 \
  -v ./kg/neo4j/data:/data \
  -v ./kg/neo4j/logs:/logs \
  neo4j:latest
