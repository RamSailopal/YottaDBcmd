Docker stack with both client and server.

To run:

    docker-compose up -d
    
    docker exec -it yottaclient /bin/bash
    
    ./yottacmd-remote -U yotta -P Access-please -s yotta-server -p 4001 -c 'command S ^RAM("TESTER")="TEST"'
    
    ./yottacmd-remote -U yotta -P Access-please -s yotta-server -p 4001 -c 'globalview ^RAM'
