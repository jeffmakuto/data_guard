const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const TerserWebpackPlugin = require('terser-webpack-plugin');
const CssMinimizerWebpackPlugin = require('css-minimizer-webpack-plugin');

module.exports = (env, argv) => {
  const isProduction = argv.mode === 'production';

  return {
    entry: './src/index.js',
    output: {
      filename: isProduction ? '[name].[contenthash].js' : '[name].bundle.js',
      path: path.resolve(__dirname, 'dist'),
      publicPath: '/',
    },
    mode: isProduction ? 'production' : 'development',
    devtool: isProduction ? 'source-map' : 'inline-source-map',
    devServer: {
      contentBase: path.resolve(__dirname, 'dist'),
      historyApiFallback: true,
      open: true,
      compress: true,
      hot: true,
      port: 3000,
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env', '@babel/preset-react'],
            },
          },
        },
        {
          test: /\.css$/,
          use: [
            isProduction ? MiniCssExtractPlugin.loader : 'style-loader',
            'css-loader',
          ],
        },
        {
          test: /\.(png|jpg|gif|svg)$/,
          type: 'asset/resource',
        },
        {
          test: /\.html$/,
          use: 'html-loader',
        },
      ],
    },
    plugins: [
      new CleanWebpackPlugin(),
      new HtmlWebpackPlugin({
        template: './public/index.html',
        filename: 'index.html',
      }),
      new MiniCssExtractPlugin({
        filename: isProduction ? '[name].[contenthash].css' : '[name].css',
      }),
    ],
    optimization: {
      minimize: isProduction,
      minimizer: [
        new TerserWebpackPlugin({
          parallel: true,
        }),
        new CssMinimizerWebpackPlugin(),
      ],
      splitChunks: {
        chunks: 'all',
      },
      runtimeChunk: 'single',
    },
    resolve: {
      extensions: ['.js', '.jsx'],
    },
  };
};
