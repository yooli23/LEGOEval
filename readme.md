![](https://github.com/yooli23/LEGOEval/blob/master/readme_banner.png)
# LEGOEval
LEGOEval is a toolkit for dialogue system evaluation via crowdsourcing, see our [demo video](https://www.youtube.com/watch?v=Dg6mafRGOpg&ab_channel=JoshArnold).

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

## Documentation
Check out our docs for the following steps, [here](https://legodocs.herokuapp.com/).

## Citing
If you use LEGOEval in your research, please cite [LEGOEval: An Open-Source Toolkit for Dialogue System Evaluation via Crowdsourcing](https://arxiv.org/pdf/2105.01992.pdf).
```
@misc{li2021legoeval,
      title={LEGOEval: An Open-Source Toolkit for Dialogue System Evaluation via Crowdsourcing}, 
      author={Yu Li and Josh Arnold and Feifan Yan and Weiyan Shi and Zhou Yu},
      year={2021},
      eprint={2105.01992},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
