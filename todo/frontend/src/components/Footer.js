import React from 'react'


const FooterItem = ({footer}) => {
    return (
        <tr>
            <td>
                {footer.authors_nickname}
            </td>
            <td>
                {footer.date}
            </td>
            <td>
                {footer.copyright}
            </td>
        </tr>
    )
}


const FooterList = ({footers}) => {
    return (
        <table>
            <th>
                Authors_nickname
            </th>
            <th>
                Date
            </th>
            <th>
                Copyright
            </th>
            {footers.map((footer) => <FooterItem footer={footer} />)}
        </table>
    )
}


export default FooterList
