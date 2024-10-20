# FaceAnomCli(fac)

fac is a tool which can be used to record vidoes by anominizing the face.


## Installation

(**Use of virtual env is encouraged**)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fac.

```bash
git clone https://github.com/grishrana/faceAnomCli.git
cd faceAnomCli
pip install -e
```

## Usage
```bash
> fac --help
Usage: fac [OPTIONS] COMMAND [ARGS]...

  Entry point to preview the webcam.

Options:
  --help  Show this message and exit.

Commands:
  webcam


> fac webcam --help
Usage: fac webcam [OPTIONS]

Options:
  -o, --output PATH  Enter output filename or path/filename  [default:
                     (fac_{current data and time}.mp4)]
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
