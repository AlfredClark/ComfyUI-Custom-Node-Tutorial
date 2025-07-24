import {app} from "../../scripts/app.js";
import {api} from "../../scripts/api.js";

app.registerExtension({
    name: "InteractExtension",
    // 注册节点前添加回调函数
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        // 只针对InteractNode类型的节点
        if (nodeData.name !== "InteractNode") {
            return;
        }
        // 获得原始onNodeCreated函数
        const onNodeCreated = nodeType.prototype.onNodeCreated;
        // 替换为自定义的onNodeCreated函数
        nodeType.prototype.onNodeCreated = function () {
            // 备份节点
            const node = this;
            // 执行原始onNodeCreated函数
            const r = onNodeCreated ? (
                onNodeCreated.apply(this, arguments)
            ) : void 0;
            // 通过组件名称获得组件
            const model_type = this.widgets.find(w => w.name === "model_type");
            const model_name = this.widgets.find(w => w.name === "model_name");
            // 同时获得两个组件时执行替换
            if (model_type && model_name) {
                // 替换model_type的回调函数
                model_type.callback = (value) => {
                    // 设置画布
                    node.setDirtyCanvas(true, true);
                    // 服务器交互
                    interact_with_server(node.id, value, model_name);
                };

                // 初始化时触发一次回调
                model_type.callback(model_type.value);
            }
            return r
        };

        // 配置加载后的初始化
        nodeType.prototype.onConfigure = function () {
            const node = this
            const model_type = this.widgets.find(w => w.name === "model_type");
            const model_name = this.widgets.find(w => w.name === "model_name");
            interact_with_server(node.id, model_type.value, model_name);
        };
    }
});

// 更新ModelName数据
function updateModelName(node, names) {
    console.log(node.value)
    console.log(node.options)
    // 更新选项列表
    node.options.values = names;
    node.value = names[0]
    // 通知ComfyUI更新widget状态
    if (node.callback) {
        node.callback(node.value);
    }
}

// 与服务器异步交互的方法
async function interact_with_server(node_id, value, node) {
    // 构建表单数据
    const body = new FormData();
    body.append('node_id', node_id);
    body.append('type', value);
    // 访问API
    let resp = await api.fetchApi("/interact_node", {method: "POST", body,});
    // 请求成功则更新列表
    if (resp.status === 200) {
        const data = await resp.json()
        console.log(data)
        updateModelName(node, data.names);
    }
}