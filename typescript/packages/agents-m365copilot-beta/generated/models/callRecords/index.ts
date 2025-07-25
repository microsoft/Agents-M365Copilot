/* tslint:disable */
/* eslint-disable */
// Generated by Microsoft Kiota
// @ts-ignore
import { deserializeIntoIdentity, serializeIdentity, type Identity } from '../index.js';
// @ts-ignore
import { type Parsable, type ParseNode, type SerializationWriter } from '@microsoft/kiota-abstractions';

/**
 * Creates a new instance of the appropriate class based on discriminator value
 * @param parseNode The parse node to use to read the discriminator value and create the object
 * @returns {UserIdentity}
 */
// @ts-ignore
export function createUserIdentityFromDiscriminatorValue(parseNode: ParseNode | undefined) : ((instance?: Parsable) => Record<string, (node: ParseNode) => void>) {
    return deserializeIntoUserIdentity;
}
/**
 * The deserialization information for the current model
 * @param UserIdentity The instance to deserialize into.
 * @returns {Record<string, (node: ParseNode) => void>}
 */
// @ts-ignore
export function deserializeIntoUserIdentity(userIdentity: Partial<UserIdentity> | undefined = {}) : Record<string, (node: ParseNode) => void> {
    return {
        ...deserializeIntoIdentity(userIdentity),
        "userPrincipalName": n => { userIdentity.userPrincipalName = n.getStringValue(); },
    }
}
/**
 * Serializes information the current object
 * @param isSerializingDerivedType A boolean indicating whether the serialization is for a derived type.
 * @param UserIdentity The instance to serialize from.
 * @param writer Serialization writer to use to serialize this model
 */
// @ts-ignore
export function serializeUserIdentity(writer: SerializationWriter, userIdentity: Partial<UserIdentity> | undefined | null = {}, isSerializingDerivedType: boolean = false) : void {
    if (!userIdentity || isSerializingDerivedType) { return; }
    serializeIdentity(writer, userIdentity, isSerializingDerivedType)
    writer.writeStringValue("userPrincipalName", userIdentity.userPrincipalName);
}
export interface UserIdentity extends Identity, Parsable {
    /**
     * The userPrincipalName property
     */
    userPrincipalName?: string | null;
}
/* tslint:enable */
/* eslint-enable */
