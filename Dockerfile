#########################
## Two container build ##
#########################

# Fisrst container - ALSE MG Docker image
FROM python:3.10-bullseye as build
# Install requirements
RUN pip3 install -U pip sphinx sphinx-rtd-theme sphinx-multiversion
# Change working directory
WORKDIR documents
# It's necessary to copy all conent becouse of sphinx-multiversions dependency .git dir
# and files integrity
ADD . .
# Build documentation
RUN sphinx-multiversion docs/ build/html



# Second container with lightweight
FROM nginx:alpine-slim

# Set timezone
ENV TZ=Europe/Moscow \
    DEBIAN_FRONTEND=noninteractive

#COPY sphinx.conf /etc/nginx/conf.d/default.conf

# Copy documentation from build container
COPY --from=build /documents/docs/master/ /usr/share/nginx/html/
