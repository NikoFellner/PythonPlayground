import requests
from pathlib import Path
from tqdm import tqdm
from loguru import logger

# Directory where you store MIR-Flickr images (or where to download)
IMAGE_ROOT = Path("data/IND_Cluster/images")
CLUSTER_FILE = Path("data/IND_Cluster/IND_clusters.txt")  # or NIND_clusters.txt


def load_clusters(cluster_file):
    """
    Load cluster file: each line is space-separated Flickr photo IDs belonging to one cluster.
    Returns dict photo_id -> cluster_id.
    """
    photo2cluster = {}
    clusters = []
    with open(cluster_file, "r") as f:
        for idx, line in enumerate(f):
            parts = line.strip().split()
            if not parts:
                continue
            cluster_id = idx
            for pid in parts:
                photo2cluster[pid] = cluster_id
            clusters.append(parts)
    return photo2cluster, clusters


def download_image(meta, save_path):
    """
    meta = dict with keys: id, farm, server, secret
    """
    url = f"https://farm{meta['farm']}.staticflickr.com/{meta['server']}/{meta['id']}_{meta['secret']}.jpg"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(resp.content)
        return True
    except Exception as e:
        print(f"Failed to download {meta['id']}: {e}")
        return False



def main():
    IMAGE_ROOT.mkdir(exist_ok=True)

    photo2cluster, clusters = load_clusters(CLUSTER_FILE)
    print(f"Loaded {len(clusters)} clusters, {len(photo2cluster)} images mapped.")

    labels_file = IMAGE_ROOT / "labels.csv"
    with open(labels_file, "w") as lf:
        lf.write("photo_id,cluster_id,filepath\n")

        for pid, cluster_id in tqdm(photo2cluster.items()):
            subdir = IMAGE_ROOT / str(cluster_id)
            subdir.mkdir(exist_ok=True)
            save_path = subdir / f"{pid}.jpg"
            success = download_image(pid, save_path)
            if success:
                lf.write(f"{pid},{cluster_id},{save_path}\n")
                logger.info(f"SUCCESS: {pid},{cluster_id},{save_path}\n")
            else:
                lf.write(f"{pid},{cluster_id},\n")
                logger.info(f"FAILED: {pid},{cluster_id}\n")
    print("Done.")


if __name__ == "__main__":
    main()
