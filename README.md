
```bash
sudo docker rm -f $(sudo docker ps -aq) && sudo docker compose -f dev.docker-compose.yml up -d
```