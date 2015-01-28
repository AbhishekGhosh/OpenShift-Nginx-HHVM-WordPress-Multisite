# OpenShift HHVM Cartridge

Nginx + HHVM 3.5.0 + WordPress as Normal Version to Allow Mod

GNU GPL 3.0 material, no warrenty of working rightly! 
It is Beta.

## Usage

### Command line

Create an empty DIY cartige. clone this repo and push it. You can not directly run rhc command as this repo is bigger than max allowed limit.

### Updating Cartridge

```bash
rhc ssh get-your-url
# In SSH
cd nginx-hhvm
bin/control update
```

## HHVM

The HHVM packaged with this cartridge is built directly from the newest released version of HHVM source and WordPress. You will need a MySQl cart and add the database details to install WordPress. 
You can change to multi, you can do anything.

## Configuration

nginx .conf files should be inside config/nginx.d/

config.hdf should be inside config/hhvm.d/
