// Last updated: 5/8/2026, 11:06:35 PM
/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.sort((a, b) => fn(a) - fn(b))
};

/*
Initial attempt with Insertion sort (timed out):
for (let i = 1; i < arr.length; i++) {
        let x = fn(arr[i]);
        let y = arr[i];
        let j = i-1;

        while (j >= 0 && fn(arr[j]) > x) {
            arr[j+1] = arr[j];
            j = j-1;
        }
        arr[j+1] = y;
    }

    return arr;
*/