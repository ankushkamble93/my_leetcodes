class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            ipsection = queryIP.split(".")
            if len(ipsection) != 4:
                return "Neither"
            for section in ipsection:
                if not section.isdigit() or int(section) > 255 or (section[0] == "0" and len(section) > 1):
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP:
            ipsection = queryIP.split(":")
            if len(ipsection) != 8:
                return "Neither"
            for section in ipsection:
                if len(section) == 0 or len(section) > 4 or not all(h in string.hexdigits for h in section):
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"