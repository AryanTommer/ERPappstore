FROM node:8 as node

WORKDIR /srv

COPY TechKiteERPappstore/core/static TechKiteERPappstore/core/static
COPY package.json package.json
COPY yarn.lock yarn.lock
COPY webpack.config.js webpack.config.js
COPY tsconfig.json tsconfig.json

RUN yarn install
RUN yarn run build


FROM python:3.6 as translations

WORKDIR /srv

RUN apt-get update && apt-get install -y gettext libgettextpo-dev

COPY requirements requirements
RUN pip install -r requirements/base.txt
RUN pip install -r requirements/development.txt

COPY TechKiteERPappstore TechKiteERPappstore
COPY manage.py manage.py
COPY locale locale

# provide a temporary secret key in order to be able to run the compile messages command
RUN echo "SECRET_KEY = 'secret'" >> TechKiteERPappstore/settings/base.py
RUN python manage.py compilemessages --settings=TechKiteERPappstore.settings.base


FROM python:3.6 as main

ARG platform
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

WORKDIR /srv

COPY requirements requirements
COPY TechKiteERPappstore TechKiteERPappstore
COPY manage.py manage.py
COPY scripts/build/start.sh start.sh

RUN rm -r TechKiteERPappstore/core/static
COPY --from=node /srv/TechKiteERPappstore/core/static TechKiteERPappstore/core/static
COPY --from=translations /srv/locale locale

RUN pip install -r requirements/base.txt
RUN pip install -r requirements/${platform}.txt

RUN groupadd TechKiteERPappstore
RUN useradd -g TechKiteERPappstore -s /bin/false TechKiteERPappstore
RUN chown -R TechKiteERPappstore:TechKiteERPappstore /srv

ENTRYPOINT ["/srv/start.sh"]
