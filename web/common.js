// 部分通用的js方法整合

// 加载CSS文件
export const loadCss = (cssFile) => {
    const cssPath = import.meta.resolve(cssFile);
    const $link = document.createElement("link");
    $link.setAttribute("rel", 'stylesheet');
    $link.setAttribute("href", cssPath);
    document.head.appendChild($link);
};

