/// <reference types="node" />
export { Object_ as Object, Array_ as Array };
/** JSON data, as returned by `JSON.parse()`. */
export declare type Value = null | boolean | number | string | Object_ | Array_;
/** JSON object values. */
interface Object_ extends Record<string, Value> {
}
/** JSON array values. */
interface Array_ extends Array<Value> {
}
/** Tests a JSON value to see if it is `null`. */
export declare function isNull(x: Value): x is null;
/** Cast a JSON value to `null`, throwing a `TypeError` if the cast fails. */
export declare function asNull(x: Value, prefix?: string): null;
/** Tests a JSON value to see if it is a boolean. */
export declare function isBoolean(x: Value): x is boolean;
/** Cast a JSON value to boolean, throwing a `TypeError` if the cast fails. */
export declare function asBoolean(x: Value, prefix?: string): boolean;
/** Tests a JSON value to see if it is a number. */
export declare function isNumber(x: Value): x is number;
/** Cast a JSON value to number, throwing a `TypeError` if the cast fails. */
export declare function asNumber(x: Value, prefix?: string): number;
/** Tests a JSON value to see if it is a string. */
export declare function isString(x: Value): x is string;
/** Cast a JSON value to string, throwing a `TypeError` if the cast fails. */
export declare function asString(x: Value, prefix?: string): string;
/** Tests a JSON value to see if it is a JSON object. */
export declare function isObject(x: Value): x is Object_;
/** Cast a JSON value to `Object`, throwing a `TypeError` if the cast fails. */
export declare function asObject(x: Value, prefix?: string): Object_;
/** Tests a JSON value to see if it is a JSON array. */
export declare function isArray(x: Value): x is Array_;
/** Cast a JSON value to `Array`, throwing a `TypeError` if the cast fails. */
export declare function asArray(x: Value, prefix?: string): Array_;
/** A more safely typed version of `JSON.parse()`. */
export declare function parse(source: string): Value;
/** A more safely typed version of `JSON.stringify()`. */
export declare function stringify(value: Value): string;
/** Synchronously reads a text file and parses it as JSON. */
export declare function loadSync(path: string, encoding?: BufferEncoding): Value;
export declare function load(path: string, encoding?: BufferEncoding): Promise<Value>;
