### Static layers

FROM alpine:3.15 AS skf-alpine37
LABEL "owner"="Glenn ten Cate" "owner.email"="glenn.ten.cate@owasp.org>"

# Installing needed binaries and deps. Then removing unneeded deps:
RUN apk update --no-cache && apk add python3=3.9.7-r4 python3-dev=3.9.7-r4 py3-pip=20.3.4-r1 bash=5.1.8-r0 git=2.34.1-r0 dos2unix=7.4.2-r0

### Dynamic layers
FROM skf-alpine37
LABEL "owner"="Glenn ten Cate" "owner.email"="glenn.ten.cate@owasp.org>"

RUN addgroup -g 1000 app
RUN adduser -u 1000 -G app -D -h /home/app app
RUN rm -rf /var/cache/apk/APKINDEX*

COPY ./ /home/app/XSS

# Switching to the new app location:
WORKDIR /home/app/XSS

RUN chown -R app:app /home/app/XSS

# Switching to the limited user
USER app

# Installing needed binaries and deps
RUN pip3 install --no-cache-dir  --user -r requirements.txt

# Fixing Windows line endings for our students:
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN find . -name "*.sh" -o -name "*.py" -o -name "*.css" -o -name "*.js" | xargs dos2unix

# Setting chmod +x on the scripts:
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN find . -name "*.sh" -o -name "*.py" -o -name "Dockerfile" | xargs chmod +x

# Starting the actual application:
ENTRYPOINT [ "python3", "./app.py" ]
