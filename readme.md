# LEGOEval
A toolkit for dialogue system evaluation via crowdsourcing.

## Install LEGOEval
LegoEval supports **Python 3.6+**. Windows is not supported currently.

### 1. Installing via pip
If you have installed **npm >= 7.7.6** and **Node.js >= 15.13.0**, you can install LegoEval via `pip`.

#### Clone the Repo
In your terminal app, paste the following command.
```bash
git clone https://github.com/yooli23/LEGOEval.git
```
#### Installing the libarary and dependencies
Installing the library and dependencies is simple using `pip`.
```bash
cd app
pip3 install -r requirements.txt
```

### 2. Installing via Docker
We also provide a dockerfile which makes it easy to distribute the environment.

Once you have installed [Docker](https://docs.docker.com/get-docker/), you can run the following commands to get the environment.

1. Build
```bash
sudo docker build https://github.com/yooli23/LEGOEval.git -t legoeval:1
```

2. Run docker
```bash
sudo docker run -it legoeval:1
```

3. Clone the code
```bash
git clone https://github.com/yooli23/LEGOEval.git
```

#### Documentation
Check out our docs for the following steps at [here](https://legodocs.herokuapp.com/).
