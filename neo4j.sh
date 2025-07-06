docker run \
  --name neo4j \
  -p 7474:7474 \
  -p 7687:7687 \
  -v $HOME/neo4j/data:/data \
  -e NEO4J_AUTH=neo4j/neo4j12345 \
  neo4j:latest
