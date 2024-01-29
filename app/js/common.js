const blockElements = [
    'div', 'section', 'article', 'aside', 'nav',
    'header', 'footer', 'main', 'form', 'fieldset', 'table'
];
const ignoredElements = ['script', 'style', 'noscript', 'br', 'hr'];

function getElementArea(element) {
    const rect = element.getBoundingClientRect();
    return rect.height * rect.width;
}

function getBackgroundColor(element) {
    const style = window.getComputedStyle(element);
    if (style.backgroundColor === 'transparent') {
        const parent = element.parentElement;
        return (parent === null || parent.tagName.toLowerCase() === 'body') ? 'rgb(255, 255, 255)' : getBackgroundColor(parent);
    }
    return style.backgroundColor;
}

function getRandomSubarray(arr, size) {
    const shuffled = arr.slice(0).sort(() => Math.random() - 0.5);
    return shuffled.slice(0, size);
}

function getVisibleChildren(element) {
    return Array.from(element.children).filter(child => isShown(child));
}

function getParents(node) {
    const result = [];
    while (node = node.parentElement) {
        result.push(node);
    }
    return result;
}

function isShown(element) {
    const style = window.getComputedStyle(element);
    return style.display !== 'none' && style.visibility !== 'hidden' && style.visibility !== 'collapse';
}

function containsTextNodes(element) {
    return Array.from(element.childNodes).some(node => node.nodeType === Node.TEXT_NODE && node.textContent.trim().length > 0);
}

function isPixel(element) {
    const rect = element.getBoundingClientRect();
    return rect.height === 1 && rect.width === 1;
}

function containsBlockElements(element, visibility = true) {
    const children = Array.from(element.children);
    for (const child of children) {
        if (blockElements.includes(child.tagName.toLowerCase())) {
            if (visibility && isShown(child)) {
                return true;
            }
            if (!visibility) {
                return true;
            }
        }
    }
    return false;
}

function isWhitespace(element) {
    return element.nodeType === Node.TEXT_NODE && element.textContent.trim().length === 0;
}
