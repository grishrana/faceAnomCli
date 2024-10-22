# FaceAnomCli(fac)

fac is a tool which can be used to record vidoes by anominizing the face.


## Installation

(**Use of virtual env is encouraged**)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fac.

```bash
git clone https://github.com/grishrana/faceAnomCli.git
cd faceAnomCli
python -m venv .env
source .env/bin/activate
pip install -e .
```

## Usage
```bash
> fac --help
Usage: fac [OPTIONS] COMMAND [ARGS]...

  Entry point to preview the webcam.

Options:
  --help  Show this message and exit.

Commands:
  image
  webcam


> fac webcam --help
Usage: fac webcam [OPTIONS]

Options:
  -o, --output PATH          Enter output filename or path/filename
                             [default: (fac_20241022_221714.mp4)]
  -fl, --flip INTEGER RANGE  1: Flips 0: Doesnot flips webcam
                             [default: (1); 0<=x<=1]
  --help                     Show this message and exit.

> fac image --help
Usage: fac image [OPTIONS] IMG_PATH

Options:
  -o, --output PATH  Enter output path for image  [default:
                     ({img_name}_fac.{img_extension})]
  --help             Show this message and exit.
```

## Future Features:
1. Image and Video anominizer
2. Voice anominizer

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
