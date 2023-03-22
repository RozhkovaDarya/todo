import React from 'react'


const MenuItem = ({menu}) => {
    return (
        <tr>
            <td>
                {menu.file}
            </td>
            <td>
                {menu.change}
            </td>
            <td>
                {menu.viewing}
            </td>
        </tr>
    )
}


const MenuList = ({menu}) => {
    return (
        <table>
            <th>
                File
            </th>
            <th>
                Change
            </th>
            <th>
                Viewing
            </th>
            {menu.map((menu) => <MenuItem menu={menu} />)}
        </table>
    )
}


export default MenuList
