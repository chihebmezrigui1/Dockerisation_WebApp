# Use the official MySQL image
FROM mysql:8

# Copy initialization scripts (if any)
COPY conf/ /docker-entrypoint-initdb.d/

# Expose MySQL port
EXPOSE 5655

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=test_db
