FROM postgres:latest
ENV POSTGRES_DB ticket_db
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
COPY init.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
