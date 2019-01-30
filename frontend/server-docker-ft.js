const Webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const path = require('path');

const webpackConfig = require('./webpack.docker.config');
const notifications = require('./notifications');

const http = require('http');

const devServerOptions = {
  contentBase: path.join(__dirname, 'public'),
  publicPath: '/build/',
  historyApiFallback: true,
  port: 3000,
  compress: true,
  disableHostCheck: true,
  public: 'nginx',
  proxy: {
    '/socket.io': {
      target: 'http://localhost:4000/socket.io',
      ws: true
    }
  },
  hot: false,
};

WebpackDevServer.addDevServerEntrypoints(webpackConfig, devServerOptions);
const compiler = Webpack(webpackConfig);
const server = new WebpackDevServer(compiler, devServerOptions);
const httpServer = http.createServer((req, res) => {
  res.end();
});

const io = require('socket.io')(httpServer);

httpServer.listen(4000);

io.on('connect', (socket) => {
  socket.join('global');
  socket.emit('action', { type: 'SERVER_INITIATED_NOTIFICATION_RELOAD', message: 'connected' });
});

notifications.connect(io);

server.listen(3000, '0.0.0.0', () => {
  console.log('Starting server');
});
