const core = require("@serverless-devs/core");

/**
 * Plugin 插件入口
 * @param inputs 组件的入口参数
 * @param args 插件的自定义参数
 * @return inputs
 */

module.exports = async function index(inputs, args) {
  console.log(inputs)
  console.log(args)
  return inputs
};