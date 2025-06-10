FROM nginx:1.27.5-alpine

RUN rm /etc/nginx/conf.d/default.conf && rm -f "/var/log/nginx/*"
COPY nginx.conf /etc/nginx/

CMD ["nginx", "-g", "daemon off;"]
