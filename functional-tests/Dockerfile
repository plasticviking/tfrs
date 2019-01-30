FROM openjdk:8-stretch

RUN apt-get update && apt-get install -yq \
    chromium \
    git-core \
    xvfb \
    xsel \
    unzip \
    gradle

RUN wget -q "https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip

ADD chromium-vfb.sh /usr/bin/chromium-vfb.sh
ADD ready_wait.sh /usr/bin/ready_wait.sh

RUN ln -s /usr/bin/chromium-vfb.sh /usr/bin/google-chrome \
    && chmod 777 /usr/bin/chromium-vfb.sh

RUN chmod 777 /usr/bin/ready_wait.sh

RUN mkdir /functional-tests
ADD . /functional-tests
WORKDIR /functional-tests

CMD bash -c "source docker.env && /usr/bin/ready_wait.sh && gradle chromeHeadlessTest --tests docframework.*"


