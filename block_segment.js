// Function to check if all children of an element are ignored
function allIgnoreChildren(element, ignoredElements) {
    return Array.from(element.children).every(child => ignoredElements.includes(child.tagName.toLowerCase()));
}

// Function to segment elements based on certain conditions
function segments(element, ignoredElements, blockElements, winArea) {
    if (!element || ignoredElements.includes(element.tagName.toLowerCase()) || isPixel(element) || !isShown(element)) {
        return [];
    }

    if (blockElements.includes(element.tagName.toLowerCase())) {
        if (!containsBlockElements(element) && allIgnoreChildren(element, ignoredElements)) {
            return [];
        }
    }

    if (containsTextNodes(element) || containsBlockElements(element, blockElements.includes(element.tagName.toLowerCase()))) {
        return [element];
    }

    if (getElementArea(element) / winArea <= 0.3) {
        return [element];
    }

    let result = [];
    for (let child of element.children) {
        result = result.concat(segments(child, ignoredElements, blockElements, winArea));
    }
    return result;
}
