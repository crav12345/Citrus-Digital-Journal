#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
"""Aes_cipher.py: Implementation of the Advanced Encryption Standard (AES)"""
# ----------------------------------------------------------------------------
# author: = Christopher P. Ravosa
# course: MSCS 630L
# assignment = Final Project
# due_date: May 9, 2022
# version: 1.0
# ----------------------------------------------------------------------------

# Constant to store substitution box matrix.
S_BOX = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
     0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
     0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
     0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
     0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
     0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
     0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
     0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
     0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
     0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
     0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
     0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
     0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
     0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
     0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
     0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
     0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]

# Constant to store our round constant lookup table.
R_CON = [
    [0x8D, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
     0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A],
    [0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
     0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39],
    [0x72, 0xE4, 0xD3, 0xBD, 0x61, 0xC2, 0x9F, 0x25,
     0x4A, 0x94, 0x33, 0x66, 0xCC, 0x83, 0x1D, 0x3A],
    [0x74, 0xE8, 0xCB, 0x8D, 0x01, 0x02, 0x04, 0x08,
     0x10, 0x20, 0x40, 0x80, 0x1B, 0x36, 0x6C, 0xD8],
    [0xAB, 0x4D, 0x9A, 0x2F, 0x5E, 0xBC, 0x63, 0xC6,
     0x97, 0x35, 0x6A, 0xD4, 0xB3, 0x7D, 0xFA, 0xEF],
    [0xC5, 0x91, 0x39, 0x72, 0xE4, 0xD3, 0xBD, 0x61,
     0xC2, 0x9F, 0x25, 0x4A, 0x94, 0x33, 0x66, 0xCC],
    [0x83, 0x1D, 0x3A, 0x74, 0xE8, 0xCB, 0x8D, 0x01,
     0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B],
    [0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A, 0x2F, 0x5E,
     0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A, 0xD4, 0xB3],
    [0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39, 0x72, 0xE4,
     0xD3, 0xBD, 0x61, 0xC2, 0x9F, 0x25, 0x4A, 0x94],
    [0x33, 0x66, 0xCC, 0x83, 0x1D, 0x3A, 0x74, 0xE8,
     0xCB, 0x8D, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20],
    [0x40, 0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D,
     0x9A, 0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35],
    [0x6A, 0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91,
     0x39, 0x72, 0xE4, 0xD3, 0xBD, 0x61, 0xC2, 0x9F],
    [0x25, 0x4A, 0x94, 0x33, 0x66, 0xCC, 0x83, 0x1D,
     0x3A, 0x74, 0xE8, 0xCB, 0x8D, 0x01, 0x02, 0x04],
    [0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36, 0x6C,
     0xD8, 0xAB, 0x4D, 0x9A, 0x2F, 0x5E, 0xBC, 0x63],
    [0xC6, 0x97, 0x35, 0x6A, 0xD4, 0xB3, 0x7D, 0xFA,
     0xEF, 0xC5, 0x91, 0x39, 0x72, 0xE4, 0xD3, 0xBD],
    [0x61, 0xC2, 0x9F, 0x25, 0x4A, 0x94, 0x33, 0x66,
     0xCC, 0x83, 0x1D, 0x3A, 0x74, 0xE8, 0xCB, 0x8D]
]

# Constants to store Galois fields.
GALOIS_FIELD_2 = [
    [0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e,
     0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e],
    [0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e,
     0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e],
    [0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e,
     0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e],
    [0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e,
     0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e],
    [0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e,
     0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e],
    [0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae,
     0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe],
    [0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce,
     0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde],
    [0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee,
     0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe],
    [0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15,
     0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05],
    [0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35,
     0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25],
    [0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55,
     0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45],
    [0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75,
     0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65],
    [0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95,
     0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85],
    [0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5,
     0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5],
    [0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5,
     0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5],
    [0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5,
     0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5]
]

GALOIS_FIELD_3 = [
    [0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09,
     0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11],
    [0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39,
     0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21],
    [0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69,
     0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71],
    [0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59,
     0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41],
    [0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9,
     0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1],
    [0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9,
     0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1],
    [0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9,
     0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1],
    [0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99,
     0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81],
    [0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92,
     0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a],
    [0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2,
     0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba],
    [0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2,
     0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea],
    [0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2,
     0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda],
    [0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52,
     0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a],
    [0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62,
     0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a],
    [0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32,
     0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a],
    [0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02,
     0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a]
]


def aes_round_keys(key):
    """
    aes_round_keys

    Produces 11 round keys from a provided system key according to the key
    expansion aspect of the AES.

    parameter key: a 16 character string representing the system key
    return: an array of strings representing the 11 round keys.
    """
    # Used to return the round keys.
    round_keys = ["", "", "", "", "", "", "", "", "", "", ""]

    # Array used to split the input key into pairs of hex digits for
    # storage in the 4x4 matrix representation Ke.
    key_hex_pairs = [0] * 16

    # Split input key into pairs of hex digits and store in key_hex_pairs.
    for _ in range(0, len(key)):
        key_hex_pairs[_] = format(ord(key[_]), '02x')

    # Stores the matrix representation of our system key.
    ke = [
        [0x00] * 4,
        [0x00] * 4,
        [0x00] * 4,
        [0x00] * 4
    ]

    # Counter to keep track of which pair of hex integers is on deck.
    pairs_index = 0

    # Fill ke matrix with the hex integers.
    for row in range(len(ke)):
        for col in range(len(ke[row])):
            ke[row][col] = key_hex_pairs[pairs_index]
            pairs_index += 1

    # Stores 4x44 matrix containing representations of 11 round keys.
    w = [
        [0x00] * 44,
        [0x00] * 44,
        [0x00] * 44,
        [0x00] * 44
    ]

    # Fill first four columns of w matrix with ke values.
    for row in range(len(w)):
        for col in range(0, 4):
            w[row][col] = ke[row][col]

    # Iterate through all remaining columns of the w matrix.
    for j in range(4, len(w[0])):
        # Check if the column is not a multiple of four.
        if j % 4 != 0:
            # Perform an XOR operation on the 4th past and last column with
            # respect to the index of this column.
            w[0][j] = format(int(w[0][j - 4], 16) ^ int(w[0][j - 1], 16), '02x')
            w[1][j] = format(int(w[1][j - 4], 16) ^ int(w[1][j - 1], 16), '02x')
            w[2][j] = format(int(w[2][j - 4], 16) ^ int(w[2][j - 1], 16), '02x')
            w[3][j] = format(int(w[3][j - 4], 16) ^ int(w[3][j - 1], 16), '02x')
        # Handle column indices which ARE multiples of four.
        else:
            # Create column vector, w_new, with previous column.
            w_new = [
                w[0][j - 1],
                w[1][j - 1],
                w[2][j - 1],
                w[3][j - 1]
            ]

            # Store the first element of w_new, so we can shift left.
            temp = w_new[0]

            # Shift all elements of v_new to the left.
            for _ in range(len(w_new)):
                if _ == len(w_new) - 1:
                    w_new[_] = temp
                else:
                    w_new[_] = w_new[_ + 1]

            # Substitute each of the four bytes in w_new using the S-BOX table.
            for _ in range(len(w_new)):
                w_new[_] = aes_s_box(w_new[_])

            # Get the round constant using the R-CON search table.
            r_con = aes_r_con(j >> 2)

            # Perform XOR operation using round constant we just obtained.
            w_new[0] = format(int(r_con, 16) ^ int(w_new[0], 16), '02x')

            # Finally, w(j) can be defined as w(j) = w(j-4) XOR w_new.
            w[0][j] = format(int(w[0][j - 4], 16) ^ int(w_new[0], 16), '02x')
            w[1][j] = format(int(w[1][j - 4], 16) ^ int(w_new[1], 16), '02x')
            w[2][j] = format(int(w[2][j - 4], 16) ^ int(w_new[2], 16), '02x')
            w[3][j] = format(int(w[3][j - 4], 16) ^ int(w_new[3], 16), '02x')

    # Load 4x4 chunks of w into strings in the round_keys array.
    for row in range(len(w)):
        for col in range(len(w[0])):
            round_keys[col >> 2] += w[row][col]

    return round_keys


def aes_s_box(in_hex):
    """
    aes_s_box

    Finds the proper substitution for a hexadecimal integer in a column vector
    by utilizing the AES substitution box lookup table.

    parameter in_hex: a string representing a pair of hexadecimal digits
    return: a hexadecimal integer.
    """
    row = int(in_hex[0], 16)
    col = int(in_hex[1], 16)

    return format(S_BOX[row][col], '02x')


def aes_r_con(key_round):
    """
    aes_r_con

    Utilizes the AES round constant lookup table to find the constant for a
    given round of AES key scheduling.

    parameter key_round: an integer >= 0
    return: a hexadecimal integer representing an AES round constant.
    """
    return format(R_CON[0][key_round], '02x')


def aes_state_xor(s_hex, key_hex):
    """
    aes_state_xor

    Performs the AES 'add round key' operation, producing an output matrix
    which represents the XOR of the corresponding input matrices.

    parameter s_hex: a 4x4 matrix of integers
    parameter key_hex: a 4x4 matrix of hex integers
    return: a 4x4 matrix representing the XOR of the input matrices.
    """
    # Resulting XOR matrix which will be returned.
    out_state_hex = [
        [0x00] * 4,
        [0x00] * 4,
        [0x00] * 4,
        [0x00] * 4
    ]

    # Perform an XOR operation on each of the columns of the two input
    # matrices, storing the result in out_state_hex.
    for row in range(len(out_state_hex)):
        out_state_hex[row][0] = format(
            int(s_hex[row][0], 16) ^ int(key_hex[row][0], 16), '02x'
        )
        out_state_hex[row][1] = format(
            int(s_hex[row][1], 16) ^ int(key_hex[row][1], 16), '02x'
        )
        out_state_hex[row][2] = format(
            int(s_hex[row][2], 16) ^ int(key_hex[row][2], 16), '02x'
        )
        out_state_hex[row][3] = format(
            int(s_hex[row][3], 16) ^ int(key_hex[row][3], 16), '02x'
        )

    return out_state_hex


def aes_nibble_sub(in_state_hex):
    """
    aes_nibble_sub

    Creates and returns a matrix whose values represent S-Box substitutions
    performed on the input matrix's indices.

    parameter in_state_hex: a 4x4 matrix of hexadecimal integers
    return: a 4x4 matrix of S-Box substitutions of the input matrix.
    """
    # Resulting substitution matrix which will be returned.
    out_state_hex = [
        [0x00] * 4,
        [0x00] * 4,
        [0x00] * 4,
        [0x00] * 4
    ]

    # Perform S-Box substitutions on each index of in_state_hex and store the
    # results in the out_state_hex matrix.
    for row in range(len(in_state_hex)):
        for col in range(len(in_state_hex[0])):
            out_state_hex[row][col] = aes_s_box(in_state_hex[row][col])

    return out_state_hex


def aes_shift_row(in_state_hex):
    """
    aes_shift_row

    Performs a transformation on each row of an input matrix which shifts the
    values in each row left an amount based on the row index.

    parameter in_state_hex: a 4x4 matrix of hexadecimal integers
    return: a 4x4 matrix representing the transformed input matrix.
    """
    # Transform every row of in_state_hex.
    for row in range(len(in_state_hex)):
        # Shift the row as many times as needed.
        for transforms in range(row):
            # Store leading element of in_state_hex, so we can shift left.
            temp = in_state_hex[row][0]

            # Shift all elements left.
            for col in range(len(in_state_hex[row])):
                if col == len(in_state_hex) - 1:
                    in_state_hex[row][col] = temp
                else:
                    in_state_hex[row][col] = in_state_hex[row][col + 1]

    return in_state_hex


def aes_mix_column(s):
    """
    aes_mix_column

    Performs the 'mix column' operation of AES to transform the input matrix
    to a further diffused matrix. This is done by performing a number of
    multiplication operations over Galois fields.

    parameter s: a 4x4 state matrix of hexadecimal integers
    return: a 4x4 matrix representing the AES mixed input matrix.
    """
    s_prime = [
        [0x00] * 4,
        [0x00] * 4,
        [0x00] * 4,
        [0x00] * 4
    ]

    # Perform multiplications over Galois fields to compute mix on each column
    # in s.
    for col in range(len(s[0])):
        # Formula for row 1.
        s_prime[0][col] = format(
            int(gf2(s[0][col]), 16) ^
            int(gf3(s[1][col]), 16) ^
            int(s[2][col], 16) ^
            int(s[3][col], 16)
            , '02x'
        )

        # Formula for row 2.
        s_prime[1][col] = format(
            int(s[0][col], 16) ^
            int(gf2(s[1][col]), 16) ^
            int(gf3(s[2][col]), 16) ^
            int(s[3][col], 16)
            , '02x'
        )

        # Formula for row 3.
        s_prime[2][col] = format(
            int(s[0][col], 16) ^
            int(s[1][col], 16) ^
            int(gf2(s[2][col]), 16) ^
            int(gf3(s[3][col]), 16)
            , '02x'
        )

        # Formula for row 4.
        s_prime[3][col] = format(
            int(gf3(s[0][col]), 16) ^
            int(s[1][col], 16) ^
            int(s[2][col], 16) ^
            int(gf2(s[3][col]), 16)
            , '02x'
        )

    return s_prime


def gf2(in_hex):
    """
    gf2

    Performs a lookup to multiply a hex value by 2 over a Galois field to
    complete the 'mix columns' step of AES.

    parameter in_hex: a pair of hexadecimal digits
    return: a Galois field substitution for a hex value multiplied by 2.
    """
    row = int(in_hex[0], 16)
    col = int(in_hex[1], 16)

    return format(GALOIS_FIELD_2[row][col], '02x')


def gf3(in_hex):
    """
    gf3

    Performs a lookup to multiply a hex value by 3 over a Galois field to
    complete the 'mix columns' step of AES.

    parameter in_hex: a pair of hexadecimal digits
    return: a Galois field substitution for a hex value multiplied by 3.
    """
    row = int(in_hex[0], 16)
    col = int(in_hex[1], 16)

    return format(GALOIS_FIELD_3[row][col], '02x')


def aes_encrypt(p_text, key):
    """
    aes_encrypt

    Executes an entire AES implementation to encrypt a string.

    parameter p_text: A plaintext string to be encrypted
    parameter key: The 16-bit system key w/ which the string is encrypted
    return: a ciphertext representation of the original plaintext.
    """
    # Check that the length of the plaintext is a multiple of sixteen. If this
    # is not the case, pad the plaintext with enough spaces to make it so.
    remainder = len(p_text) % 16
    if remainder > 0:
        p_text += "-" * (16 - remainder)

    # Check that the key doesn't need to be padded either.
    if len(key) < 16:
        key += "-" * (16 - len(key))

    # If the key is too long, shrink it to 16 bits.
    if len(key) > 16:
        key = key[:len(key) - (len(key) - 16)]

    # Stores the ciphertext which will be returned.
    c_text = ""

    # Complete AES encryption on every chunk of 16 characters in the plaintext.
    while p_text:
        p_text_snippet = p_text[0: 16]
        p_text = p_text[16:]

        # Stores the state matrix as it's created.
        out_state_hex = [
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4
        ]

        # Matrix to store and add keys after they've been generated.
        key_hex_matrix = [
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4
        ]

        # Matrix to store the encryption.
        s_hex = [
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4
        ]

        # Array used to split the input p_text into pairs of hex digits for
        # storage in the 4x4 matrix representation s_hex.
        p_hex_pairs = [""] * 16

        # Expand p_text_snippet into pairs of hex digits and store in p_hex_pairs.
        for _ in range(0, len(key)):
            p_hex_pairs[_] = format(ord(p_text_snippet[_]), '02x')

        # Generate the keys for each round of encryption.
        round_keys_hex = aes_round_keys(key)

        # Counter to keep track of which pair of hex integers is on deck.
        pairs_index = 0

        # Fill s_hex matrix with the plaintext hex representations.
        for row in range(len(s_hex)):
            for col in range(len(s_hex[row])):
                s_hex[row][col] = p_hex_pairs[pairs_index]
                pairs_index += 1

        # Begin 10 rounds of encryption.
        for aes_round in range(11):
            # Locates characters in round_keys_hex.
            character_index = 0

            # Convert current round key to a 4x4 matrix.
            for row in range(len(key_hex_matrix)):
                for col in range(len(key_hex_matrix[row])):
                    key_hex_matrix[row][col] = \
                        round_keys_hex[aes_round][character_index] + \
                        round_keys_hex[aes_round][character_index + 1]
                    character_index += 2

            # Perform the encryption round.
            if aes_round == len(round_keys_hex) - 1:
                out_state_hex = aes_shift_row(aes_nibble_sub(aes_state_xor(s_hex, key_hex_matrix)))
            else:
                out_state_hex = aes_mix_column(aes_shift_row(aes_nibble_sub(aes_state_xor(s_hex, key_hex_matrix))))

        # Convert result matrix to a ciphertext string.
        for state_hex in out_state_hex:
            for hex_pair in state_hex:
                c_text += hex_pair

    # Return the ciphertext.
    return c_text


def aes_decrypt(c_text, key):
    """
    aes_decrypt

    Executes an entire AES implementation to decrypt a string.

    parameter c_text: A ciphertext string to be decrypted
    parameter key: The 16-bit system key w/ which the string was encrypted
    return: a plaintext representation of the original plaintext.
    """
    # We know the c_text is divisible by 16, so we don't need to touch it. We
    # do still need to check that the key doesn't need to be padded.
    if len(key) < 16:
        key += "-" * (16 - len(key))

    # If the key is too long, shrink it to 16 bits.
    if len(key) > 16:
        key = key[:len(key) - (len(key) - 16)]

    # Stores the plaintext which will be returned.
    p_text = ""

    # Complete AES decryption on each chunk of 32 bits in the ciphertext.
    # NOTE: c_text doesn't need to be expanded because it's already hex pairs.
    while c_text:
        c_text_snippet = c_text[0: 32]
        c_text = c_text[32:]

        # Stores the state matrix as it's created.
        out_state_hex = [
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4
        ]

        # Matrix to store and add keys after they've been generated.
        key_hex_matrix = [
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4
        ]

        # Matrix to store the decryption.
        s_hex = [
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4,
            [0x00] * 4
        ]

        # Generate the keys for each round of encryption and reverse it for
        # decryption.
        round_keys_hex = aes_round_keys(key)[::-1]

        # Counter to keep track of which pair of hex integers is on deck.
        pairs_index = 0

        # Fill s_hex matrix with the ciphertext hex pairs.
        for row in range(len(s_hex)):
            for col in range(len(s_hex[row])):
                pair = c_text_snippet[pairs_index] + c_text_snippet[pairs_index + 1]
                s_hex[row][col] = pair
                pairs_index += 2

        # Begin 10 rounds of decryption.
        for aes_round in range(11):
            # Locates characters in round_keys_hex.
            character_index = 0

            # Convert current round key to a 4x4 matrix.
            for row in range(len(key_hex_matrix)):
                for col in range(len(key_hex_matrix[row])):
                    key_hex_matrix[row][col] = \
                        round_keys_hex[aes_round][character_index] + \
                        round_keys_hex[aes_round][character_index + 1]
                    character_index += 2

            # Perform the decryption round.
            if aes_round == len(round_keys_hex) - 1:
                out_state_hex = aes_shift_row(aes_nibble_sub(aes_state_xor(s_hex, key_hex_matrix)))
            else:
                out_state_hex = aes_mix_column(aes_shift_row(aes_nibble_sub(aes_state_xor(s_hex, key_hex_matrix))))

            # TODO: Convert result back to ASCII characters.


def print_matrix(matrix):
    """
    print_matrix

    Prints the contents of a 2D array. Used primarily for debugging.

    parameter matrix: a 2D array of any height and width
    """
    for row in range(len(matrix)):
        print("[", end=" ")
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=" ")
        print("]")
