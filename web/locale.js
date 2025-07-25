// 本地化扩展脚本
import {app} from "../../scripts/app.js";

// 节点注册名
const node_comfyClass = 'LocaleNode'

// 本地化字典
const locale = {
    "zh": {
        "Locale Node": "本地化节点",
        "input_int": "整数输入",
        "input_float": "浮点输入",
        "input_string": "字符输入",
        "input_number": "数值输入",
        "input_optional": "可选图像",
        "output_int": "整数输出",
        "output_float": "浮点输出",
        "output_string": "字符输出",
        "output_number": "数值输出",
        "output_image": "图像输出"
    }
}

// 注册拓展脚本
app.registerExtension({
    // 拓展名称，注意要保持唯一性
    name: "LocaleExtension",
    // 对每种节点类型调用一次，用于修改节点的行为
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeType.comfyClass === node_comfyClass) {
            // 接收本地化类型
            app.locale_name = nodeData.input.hidden.locale_name
        }
    },
    // 节点创建后进行本地化
    async nodeCreated(node) {
        if (node.comfyClass === node_comfyClass) {
            // 获得本地化类型
            let locale_name = app.locale_name

            if (Object.keys(locale).includes(locale_name)) {
                let localized_names = locale[locale_name]
                // 节点标题本地化
                node.title = localized_names[node.title]
                // 输入插槽本地化
                node.inputs.forEach(input => {
                    input.localized_name = localized_names[input.localized_name]
                })
                // 输出插槽本地化
                node.outputs.forEach(output => {
                    output.localized_name = localized_names[output.localized_name]
                })
                // 组件标签本地化
                node.widgets.forEach(widget => {
                    widget.label = localized_names[widget.label]
                })
            }
        }
    },
})
