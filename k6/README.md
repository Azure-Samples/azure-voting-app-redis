# K6 Scripts for Load Testing

Build a docker image for k6:

```
docker pull loadimpact/k6
```

Set parameters in the `load-test.js` file, in particular lines 5, 6, and 25.
To launch a load test, run the Javascript file inside the docker container

```
docker run -i loadimpact/k6 run - <load-test.js
```