sudo apt install \
  git \
  gzip \
  libftdi1-2 \
  libftdi1-dev \
  libhidapi-hidraw0 \
  libhidapi-dev \
  libudev-dev \
  zlib1g-dev \
  cmake \
  pkg-config \
  make \
  g++

git submodule init
git submodule update

cd openFPGALoader
sudo cp 99-openfpgaloader.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger # force udev to take new rule
sudo usermod -a $USER -G plugdev # add user to plugdev group

mkdir -p install
mkdir -p build
cd build
rm -rf ./*
cmake -DCMAKE_INSTALL_PREFIX=../../gui ..
make -j$(nproc) && make install