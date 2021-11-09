{
  description = "Python Environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url  = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { 
          inherit system;
        };
      in
      with pkgs;
      {
        devShell = mkShell {
          buildInputs = [
            exa
            pkgs.python3
            pkgs.python3.pkgs.colorama
            pkgs.python3.pkgs.pyfiglet
            pkgs.python3.pkgs.setuptools
          ];

          shellHook = ''
            alias ls='exa --icons'
            export PIP_PREFIX=$(pwd)/_build/pip_packages
            export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
            export PATH="$PIP_PREFIX/bin:$PATH"
            unset SOURCE_DATE_EPOCH
          '';
        };
      }
    );
}


