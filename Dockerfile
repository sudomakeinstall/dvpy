ARG BASEIMAGEVERSION
FROM tensorflow/tensorflow:${BASEIMAGEVERSION}

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  openssh-client \
  ca-certificates \
  git \
  vim \
  zsh \
  curl \
  && rm -rf /var/lib/apt/lists/*

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

RUN pip install --upgrade pip

ADD . /code

RUN pip install -e /code/
RUN pip install black pytest
