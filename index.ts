function __checkErrors(n: number) {
    if (typeof n !== 'number')
        throw new TypeError(`"n" must be a number. Got "${n}" of type "${typeof n}".`);
}
function __isInteger(num: number) {
	return (
		Number?.isInteger?.(num) ||
		(num < 0 ? Math.ceil(num) : Math.floor(num)) === num
	);    
}    
/**
 * Computes and returns the factorial of `n`. 
 * Returns -1 if `n` is negative, or `NaN` if it's infinite, itself `NaN` or a float. 
 *
 * @param n The number for which the factorial is to be calculated.
 * @returns `n!`
 */
export function factorial(n: number) {
    __checkErrors(n);
	if (isNaN(n) || !__isInteger(n) || (n >= Infinity || n <= -Infinity)) return NaN;
	let fact = 1;
	if (n < 0) return -1;
	else {
		for (let i = 1; i <= n; i++) {
			fact *= i;
		}    
	}    
	return fact;
}    
