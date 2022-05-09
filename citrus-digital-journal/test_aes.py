#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
"""Test_aes.py: Test suite for AES code for Citrus Digital Journal."""
# ----------------------------------------------------------------------------
# author: = Christopher P. Ravosa
# course: MSCS 630L
# assignment = Final Project
# due_date: May 9, 2022
# version: 1.0
# ----------------------------------------------------------------------------

import unittest
import aes_cipher as aes


class TestAES(unittest.TestCase):
    def test_aes_round_keys(self):
        self.assertEqual(
            aes.aes_round_keys(
                "aaaaaaaaaaaaaaaa"
            ),
            [
                '61616161616161616161616161616161',
                '8fee8fee8eef8eef8eef8eef8eef8eef',
                '52bc33dd51be30df51be30dfa649c728',
                'c874479acf71419e65dbeb34672ee9c1',
                'cbbff862d7a6e7791dc62d19dff118d9',
                '6dd22a4803a5423b28eec3da75849c45',
                'af7d571f54f1b38846a86bb127a33f7a',
                '2b56011e9c6dde569c345feee7447b01',
                '1a4c4d53b4d90751e0d48b6595d1aaab',
                'd09cd182f92027768256ddb878a903a8',
                'de42931195b592e44016cb736bc2c169'
            ]
        )
        self.assertEqual(
            aes.aes_round_keys(
                "abababababababab"
            ),
            [
                '61626162616261626162616261626162',
                'caa8c9abcba9c8aacba9c8aacba9c8aa',
                '64cc05ae67ce06ac67ce06aca900c862',
                'f13d3896f6383e92cd0305a94d4d85e7',
                'b68bb325251d23b1595a5ff6dd9015f2',
                '6ee55673677a59e8d08ad523e2726795',
                'd5306615413b628afa70a5866d1f78ed',
                'ebdbbda8053e5cd6afdf7afc342b53be',
                '9d46fb53b58bd70101dea458f6dd8e30',
                'fabc4714df54838205db7f271bc64878',
                'df6324301347c446b9621d3ae1276f17'
            ]
        )
        self.assertEqual(
            aes.aes_round_keys(
                "zzzzzzzzzzzzzzzz"
            ),
            [
                '7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a',
                'a1dba1dba0daa0daa0daa0daa0daa0da',
                'f42f8e55f72d8d57f72d8d5719c363b9',
                'ab840a5fac810c5ba18c0156e52645fc',
                '9a1e144b1d9c90cb119d9cca2a0c49b5',
                '958b9fd469f565aec459c50f9995dc69',
                '51da45911fea8f213d64a1aed14498f1',
                'ec3673e2fb119ebf9cf859f750148c7d',
                '645221c393821ca3639bc235c8dc502d',
                '752706c505879b38bb20e2d7e63a6a47',
                '446365a00b8c172f1b3bd90e407a1057'
            ]
        )
        self.assertEqual(
            aes.aes_round_keys(
                "abcabcabcabcabca"
            ),
            [
                '61626361626361626361626361626361',
                'caa8cbaa99fa9bf98ced8fec8eec8fee',
                '51f9329857ad36cfa449c62a22ce41af',
                'df26148cb21f29e6dd94527864aaeb44',
                '597f6be70e1138dec652007800aa4105',
                '542b40a7b2a39b45adffff87943e7f7a',
                '1a3171d6a5069dd8778877f0c8f689f3',
                '3b0a7bad292fb26a7af285753ec841b2',
                'b9b3c865b49b29434dbf3a4fab632290',
                'b80bc3a630ab82c12d92a8e7e685a737',
                'f6fd3e98a40f8d4cb7258d6ac247e0d7'
            ]
        )
        self.assertEqual(
            aes.aes_round_keys(
                "a1b2c3d4e5f6g7h8"
            ),
            [
                '61316232633364346535663667376838',
                '78492b19665531056257310744731b23',
                '1158736aa3f6c7c24413222590e3f8db',
                '30681b719c6aad6ffdeecce992718952',
                '90f8e39282e8452afd13df363140c99b',
                '659d7eec876f2a00e9fa25137e3ef76c',
                '26bbc529fa95bfbfb9436675b08e7915',
                '6ed5103967f24df2e0a3c5b0159be2f7',
                '67b2a29b80723fcd882bee5e079c7e89',
                'c173d14ad8aa95582f04eab4138ff178',
                '9dee3f7555ff6a3293977dc9c54abbc3'
            ]
        )

    def test_aes_s_box(self):
        self.assertEqual(aes.aes_s_box("62"), "aa")
        self.assertEqual(aes.aes_s_box("c8"), "e8")
        self.assertEqual(aes.aes_s_box("9f"), "db")

    def test_aes_r_con(self):
        self.assertEqual(aes.aes_r_con(8), "80")
        self.assertEqual(aes.aes_r_con(9), "1b")
        self.assertEqual(aes.aes_r_con(10), "36")

    def test_aes_state_xor(self):
        self.assertEqual(
            aes.aes_state_xor(
                [
                    ["54", "4f", "4e", "20"],
                    ["77", "6e", "69", "54"],
                    ["6f", "65", "6e", "77"],
                    ["20", "20", "65", "6f"]
                ],
                [
                    ["54", "73", "20", "67"],
                    ["68", "20", "4b", "20"],
                    ["61", "6d", "75", "46"],
                    ["74", "79", "6e", "75"]
                ]
            ),
            [
                ["00", "3c", "6e", "47"],
                ["1f", "4e", "22", "74"],
                ["0e", "08", "1b", "31"],
                ["54", "59", "0b", "1a"]
            ]
        )

    def test_aes_nibble_sub(self):
        self.assertEqual(
            aes.aes_nibble_sub(
                [
                    ["00", "3c", "6e", "47"],
                    ["1f", "4e", "22", "74"],
                    ["0e", "08", "1b", "31"],
                    ["54", "59", "0b", "1a"]
                ]
            ),
            [
                ["63", "eb", "9f", "a0"],
                ["c0", "2f", "93", "92"],
                ["ab", "30", "af", "c7"],
                ["20", "cb", "2b", "a2"]
            ]
        )

    def test_aes_inv_nibble_sub(self):
        self.assertEqual(
            aes.aes_inv_nibble_sub(
                [
                    ["63", "eb", "9f", "a0"],
                    ["c0", "2f", "93", "92"],
                    ["ab", "30", "af", "c7"],
                    ["20", "cb", "2b", "a2"]
                ]
            ),
            [
                ["00", "3c", "6e", "47"],
                ["1f", "4e", "22", "74"],
                ["0e", "08", "1b", "31"],
                ["54", "59", "0b", "1a"]
            ]
        )

    def test_aes_shift_row(self):
        self.assertEqual(
            aes.aes_shift_row(
                [
                    ["63", "eb", "9f", "a0"],
                    ["c0", "2f", "93", "92"],
                    ["ab", "30", "af", "c7"],
                    ["20", "cb", "2b", "a2"]
                ]
            ),
            [
                ["63", "eb", "9f", "a0"],
                ["2f", "93", "92", "c0"],
                ["af", "c7", "ab", "30"],
                ["a2", "20", "cb", "2b"]
            ]
        )

    def test_aes_inv_shift_row(self):
        self.assertEqual(
            aes.aes_inv_shift_row(
                [
                    ["63", "eb", "9f", "a0"],
                    ["2f", "93", "92", "c0"],
                    ["af", "c7", "ab", "30"],
                    ["a2", "20", "cb", "2b"]
                ]
            ),
            [
                ["63", "eb", "9f", "a0"],
                ["c0", "2f", "93", "92"],
                ["ab", "30", "af", "c7"],
                ["20", "cb", "2b", "a2"]
            ]
        )

    def test_aes_mix_column(self):
        self.assertEqual(
            aes.aes_mix_column(
                [
                    ["63", "eb", "9f", "a0"],
                    ["2f", "93", "92", "c0"],
                    ["af", "c7", "ab", "30"],
                    ["a2", "20", "cb", "2b"]
                ]
            ),
            [
                ["ba", "84", "e8", "1b"],
                ["75", "a4", "8d", "40"],
                ["f4", "8d", "06", "7d"],
                ["7a", "32", "0e", "5d"]
            ]
        )

    def test_aes_inv_mix_column(self):
        self.assertEqual(
            aes.aes_inv_mix_column(
                [
                    ["ba", "84", "e8", "1b"],
                    ["75", "a4", "8d", "40"],
                    ["f4", "8d", "06", "7d"],
                    ["7a", "32", "0e", "5d"]
                ]
            ),
            [
                ["63", "eb", "9f", "a0"],
                ["2f", "93", "92", "c0"],
                ["af", "c7", "ab", "30"],
                ["a2", "20", "cb", "2b"]
            ]
        )

    def test_aes_encrypt(self):
        self.assertEqual(
            aes.aes_encrypt("Hello World!!!!!", "aaaaaaaaaaaaaaaa"),
            "90cc16ff2aa63d2d790023da52d611e1"
        )
        self.assertEqual(
            aes.aes_encrypt("One two three fo", "abcabcabcabcabca"),
            "56dc396cbc98507016762ee36c5c8544"
        )
        self.assertEqual(
            aes.aes_encrypt("12345678901234567", "kappasigmakappasigma"),
            "d78000a10c0d373e4297266c26741fba2b3f299bb81e5cdd87b89a060748b561"
        )
        self.assertEqual(
            aes.aes_encrypt("12345678901234567890", "kappasig"),
            "0a57a23646bffda32e7b75f06301b97b0670cab7ec2818f99e9cf167aff025af"
        )
        self.assertEqual(
            aes.aes_encrypt(
                "12345678901234567890123456789012345678",
                "abcdefghijklmnop"
            ),
            "5d85b897d098333f6f13a6bf849398843d3c600c438e02fd63c4dd89b3348eb3"
            "73efde179f418fcca25e3e1e20eb0f5b"
        )
        self.assertEqual(
            aes.aes_encrypt(
                "Today I went to see mom back at home. We ate lunch together,"
                "then I came back.",
                "kappasigmakappasigma"
            ),
            "45856b49885dac5ed32e3c5596353db8843cf2d961d3aca74986bc1e96350b0c"
            "2085fee088dcdf746db5801e2135dccdcfd083c87032bb3dd5144055215d88609"
            "c8383245732ac974986bc1e070eb561"
        )

    def test_aes_decrypt(self):
        aes.aes_decrypt("0a57a23646bffda32e7b75f06301b97b0670cab7ec2818f99e9cf167aff025af", "kappasig")
