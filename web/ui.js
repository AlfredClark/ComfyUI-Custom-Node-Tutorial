import {app} from "../../scripts/app.js";
import {loadCss} from "./common.js";

app.registerExtension({
    name: "UIExtension",
    // 前端启动后加载CSS
    async setup() {
        loadCss("./ui.css")
    },
    // 节点注册前修改节点默认钩子
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        // 筛选节点类型
        if (nodeType.comfyClass === "UINode") {
            // 查看节点原型
            console.log(nodeType.prototype)
            // 备份原有钩子
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            // 修改自定义钩子
            nodeType.prototype.onNodeCreated = function () {
                // 获得原型结果
                const r = onNodeCreated ? (
                    onNodeCreated.apply(this, arguments)
                ) : void 0;
                // 自定义需要的功能
                console.log("custom onNodeCreated()", r);
                // 返回原型结果
                return r;
            }
        }
    },
    // 节点创建后添加自定义组件
    async nodeCreated(node) {
        // 针对UINode
        if (node.comfyClass === "UINode") {
            // 创建自定义Element
            const inputEl = document.createElement("textarea");
            // 调整Element属性
            inputEl.className = "comfy-multiline-input test-css";
            inputEl.value = "defaultVal";
            inputEl.placeholder = "placeholder";
            // 添加DOMWidget
            const addWidget = node.addDOMWidget("ui_add_text", "textarea", inputEl, {
                getValue() {
                    return inputEl.value;
                },
                setValue(v2) {
                    inputEl.value = v2;
                }
            });
            addWidget.inputEl = inputEl;
            addWidget.options.minNodeSize = [400, 200];
            // 添加事件监听
            inputEl.addEventListener("input", () => {
                // 可以进行数值处理或进行服务器请求
                console.log("Input: " + addWidget.value)
            });
            // 遍历已有的widget并绑定事件
            node.widgets.forEach(widget => {
                if (widget.name === "ui_input") {
                    widget.inputEl.addEventListener("input", function (e) {
                        addWidget.value = widget.value;
                    })
                }
            })
        }
    }
});

