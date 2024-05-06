# How to config nginx

```nginx
server {
        server_name api.devops.indepower.se;

        underscores_in_headers on; #Importent otherwice auth fails       


        location /api {
                client_max_body_size 2M;
                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_pass http://127.0.0.1:1340;

        }

```


if something fails check the other files

Like /etc/nginx/sites-available/default