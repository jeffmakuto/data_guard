import React from 'react'
import { TbDatalist } from "react-icons/tb";

import './Header.css'

const Header = ({ onClickDataList }) => {
    return (
        <div className='Data-header'>
            <h3 className='Data-title'>
                <img src='zunzun.png' alt='logo' />
                Zunzun Player
            </h3>

            <button className='Data-button' onClick={onClickDataList}>
                <TbDatalist />
            </button>
        </div>
    )
}

export default Header