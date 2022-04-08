echo "[config] Checking python version ..."
python --version

#echo "[install] Python 3.8 ..." 
#yum install -y python38 python38-devel

#alternatives --set python /usr/bin/python3.8

#echo "[config] Checking old python version post-install ..."
#python --version

#echo "[config] Checking new python version post-install ..."
#python38 --version

echo "[install] latest pip version ..."
pip install --upgrade pip

echo "[install] Python packages from pypi ..."
python3 -m pip install --no-cache-dir -r /requirements-dl.txt
