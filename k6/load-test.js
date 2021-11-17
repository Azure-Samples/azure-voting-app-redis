import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 1000,
    duration: '10m',
};

function randomExponential(rate, randomUniform) {
    // http://en.wikipedia.org/wiki/Exponential_distribution#Generating_exponential_variates
    rate = rate || 1;
  
    // Allow to pass a random uniform value or function
    // Default to Math.random()
    var U = randomUniform;
    if (typeof randomUniform === 'function') U = randomUniform();
    if (!U) U = Math.random();
  
    return -Math.log(U)/rate;
}

export default function () {
    var url = 'https://predscaling01.natzkalabs.com/loads/matrixinverse?msize=10000';     
    http.get(url);
    sleep(randomExponential(1))
}
