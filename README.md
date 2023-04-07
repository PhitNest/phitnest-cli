### Project Names

- [api](https://github.com/PhitNest/phitnest-api)
- [app](https://github.com/PhitNest/phitnest-app)
- [core](https://github.com/PhitNest/phitnest-core)
- [cli](https://github.com/PhitNest/phitnest-cli)
- [admin](https://github.com/PhitNest/phitnest-admin)
- [website](https://github.com/PhitNest/phitnest-website)
- [dgraph-js](https://github.com/PhitNest/phitnest-dgraph-js)

### Commands

```
phitnest pull                           # Pulls/Clones all projects

phitnest pull [project names...]        # Pulls all specified projects (space delimeted list)

phitnest [project name] git [options]   # Runs a git command in a specified project directory

phitnest api install                    # Installs the backend API dependencies

phitnest api dgraph                     # Starts a docker container running DGraph on port 8080

phitnest api stop-dgraph                # Stops the currently running DGraph container

phitnest api run                        # Runs the backend API locally (with authentication on sandbox mode)

phitnest api test                       # Runs all tests on the backend API
```
