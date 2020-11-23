import hydra
from omegaconf import DictConfig

from zoomClient import ZoomClient


@hydra.main("config")
def main(cfg: DictConfig):
    zoom = ZoomClient()
    zoom.start()



if __name__ == '__main__':
    main()