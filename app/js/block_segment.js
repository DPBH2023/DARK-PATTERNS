// Function to check if all children of an element are ignored
var allIgnoreChildren = function(element) {
    // If the element has no children, return false
    if (element.children.length === 0) {
        return false;
    } else {
        // Iterate through each child of the element
        for (var child of element.children) {
            // If the child is in the ignored elements list, continue to the next child
            if (ignoredElements.includes(child.tagName.toLowerCase())) {
                continue;
            } else {
                // If any child is not in the ignored elements list, return false
                return false;
            }
        }
        // If all children are in the ignored elements list, return true
        return true;
    }
};

// Function to segment elements
var segments = function(element) {
    // If the element is not defined, return an empty array
    if (!element) {
        return [];
    }

    // Get the tag name of the element in lowercase
    var tag = element.tagName.toLowerCase();

    // Check if the element is not in the ignored elements list, is not a pixel, and is shown
    if (!ignoredElements.includes(tag) && !isPixel(element) && isShown(element)) {
        // If the element is a block element
        if (blockElements.includes(tag)) {
            // If the element does not contain block elements and all children are ignored, return an empty array
            if (!containsBlockElements(element)) {
                if (allIgnoreChildren(element)) {
                    return [];
                }
                // If the element area is greater than 30% of the window area
                else {
                    // Initialize an empty array to store results
                    var result = [];
    
                    // Recursively call the segments function for each child of the element and concatenate the results
                    for (var child of element.children) {
                        result = result.concat(segments(child));
                    }
    
                    return result;
                }
            }
            // If the element contains text nodes, return the element
            else if (containsTextNodes(element)) {
                return [element];
            }
            // If the element contains block elements, recursively call the segments function for each child of the element
            else {
                var result = [];
  
                for (var child of element.children) {
                    result = result.concat(segments(child));
                }
  
                return result;
            }
        }
        // If the element is not a block element
        else {
            // If the element contains block elements and is not a block element itself
            if (containsBlockElements(element, false)) {
                var result = [];
    
                for (var child of element.children) {
                    result = result.concat(segments(child));
                }
  
                return result;
            }
            // If the element area is greater than 30% of the window area
            else {
                // Initialize an empty array to store results
                var result = [];
        
                // Recursively call the segments function for each child of the element and concatenate the results
                for (var child of element.children) {
                    result = result.concat(segments(child));
                }
        
                return result;
            }
        }
    }
    // If the element is in the ignored elements list, is a pixel, or is not shown, return an empty array
    else {
        return [];
    }
};
