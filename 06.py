def find_repeats(l, n):
    for i in range(len(l) - n):
        if len(set(l[i:i + n])) == n:
            return i + n

def part1(ll):
    return find_repeats(ll[0], 4)

def part2(ll):
    return find_repeats(ll[0], 14)

TEST_INPUT = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

TEST_SOL = [7, 19]

FULL_INPUT = "mqllsjlslffbqbsbpbcbdbfbfvbfblfltffpddsmmhjmjvmvsmvvjfvfjjfccblbddhrdhrrlcrllrrswwlpwlwwgrglrgllrrlsshffrwfwcffmrrdfdrrncrnnlvllbsbcbwcchsshsrhhbnhbbqbmmmfdfvvqpqlpqppfgpfgpfpfttwrwwwfmfpfpmmpgglwglgfgsfgsggdllfhhmchmhttlhlchhrzrszsqqqzdzrrbbpgpccmfcmcbcdcrdrzzvjjgjfgfqfcqffvbbjbjbjsbjjbhjjzjlzjznzbbjvvpssdfdvffssrffpzfppsddgwgzgccrmrmdrrzpzbbjlbjlbjbgjbjmmtmllqffpjfppzzztfzfzfmfnndmdtmmhgmmsdshdhppbnpnbpnpdndgdbdwdtwwzqqjwjpphnnjddlglzlczzdpdjdjtjtgtqtptrrbqqqspsfswsdwdjdsdcdllpzpqplqqjnjrnnvrrnrccnwnnsttqzqcqppvmvdmdjjpnppljppptpzzwbwrrqgqhghshlslblflhflfbbwhwlhwhbwbdwbdwwzlwzwhzwznwwmmrddlttdrtrsttqbqtqtdqttqwwglwlbbdmbmcbbwbnbtbmbggdqqnhqqptpdtttvcvmvmdmtdttcwclccjcrctcllrprlrqqzqccttgnntstrtqqtfthtghhvcczhhctclljcljlcjcdjcdchhmjmjjrsjszjszsbsqqpfflqffqvfqvqjjnjtthvvvcjcjrcjclcwcrcrjcrchrcrggcjjpjjbwjbwjbwjwsjjrssfggzbgzgzrzmrmwmrrczcppnmnmzzgtglljlhjlhhgzgtgddrrhvvvlhlwhlhzzgzfgzzbvbvrvllplnlqnnfvnvgvdgvddsdqsdscscjjjvrvpptgpgdgtdtdzdtztfzfszfftjftfmftmtftddjzdzssfllfsllpwpwswrwdrwrcclczlclpccdrrftrftrtltftnftfnfrnfrfgfjfttrsrqsshlhdhnnztntwwnwppwbbmrbbtntznzggthghfggttpnpnpbplpvvpmmpwmbgcpwgsfndbrclcwbdcfhlcqblplglnqpnrpjqbddfqlqvbzrtwbwzvwqntcgmzrzztlffzmfmcmfzrmcvfctmlrlbtbpsgddbqrlblsslsbcmcglzdzjzlpgzprbrmfmlzrssqddzfjzfgbpvdgrrnldmtqgtjppqqwtzbltpfgpqtdqpwhbbwblnvvpmnljdghwrbnphswhgcvhpcplbbmwprznzzwnfntfplscpflhwdmlvfwtgrjhchnmnqbfgvsglllnnzwchqtcrvqzzhttcmblcthqrjdbvpwptcqtsnwrnfbbsqlshhtqdvcfcgdlbgzqjvzvglbcdwzpzttjnsvwrdldcqqstnnfnjthncgfvggphgfgstnmvnbmtvhpmsgmrccmmslqmjfzdjnbcjbjnpmsnvmzrphhjrdrrssnclvwbnzvpccqglnpljdtwrlnvpqzlshpcmfnmrjchqvlmthqbdrlnnpwcmfnwfzpbpnrsdmrqgqsjgwttwhgqlwghjntrvdndfhdwfzbwnmbjlzbhhdqfrdtwcjjvfnjbqdmdwncfhmslflvhqdmrcdrcdrldnqdmhzsvlglgflmlhwjqvfjdmqbmgffvdmmsbrrnrlcsbncvsjffttmhnbpwmqrnvdmzhztbbsrtwgfshjnlvhqvzwpvrmqfbsszswvrglnmwlmcdpjvmqsgnjshspzwrwctwwghmgjvbthcqcrlflsnrnpwvbnghrhvzpzchjlcljplflzqdvglgtvczhnbnlqltblddslqmdpvfbstvszqdsjvgfqlmdgbsnlzlrnbbqqfqjfqhljzlpbbgbnchwljjcpzbhdmwfzmqstcwtvgtvwcpgvmhpsngrshjvzzngbhjqmcfgjjzgdzcsbsvfwmznmwnnvlbntvcmgphqmdfjvhrlldcpwgnmbpjlqflvsrwqphvlpzlsdthfzdzvlphzdbqldvggsgrcmmfmfnjsfszqqbhnmntfgrbfwtlpqgwnrcqdsmqpqbtfdsnhbdcbwcdrhrfgsctrnlchrrnlptbcnqhndcpcdrgtznqrbgjlwzsjhblptncwtqcqcbzccrnjcmfvfnzwlrgdtgcvvcprwvnrrbdjzfnlvlqfpgbpwsvcnmnmmhnshtjgrcnscljwncdjqtwhlhvcggnwbzlzvfqmcdhmzddrdhvnnjbzbtnrgqcbmzhzzfldhlwwsgztfhncgctvjvszdzhrqmzvffmhvsqssjjvrrmtwqswhwjqgbfghbgfmgqssfhbcrglnbstfnqzvwqcznzgtnvjdvhtrlmgthcrqcwbjnzddsqhzwmdwndqcplhvpbpsdthngqwmlfqfndfqbpbwwrvsrnsjbsrwjdjbcqcvdfcsscgblggwggtmbntnbmmswfhvzhltwvprdgvzwltchhzsqlpwdndwftmsgbfwbpmhsdjhwbvvpzlpspsrsnpbwtdspfvdqdjfjbzmmtbnpzrqngccrbfndnjbcjfvwjvfjdvmsqdvgctzvpzmjmjvggpqfmmrsvqbrrlwrmzhmhpcmpltwdbtmwgzrrvsdhvhlwzggjwqzpbzvzrdbptzhzcrrjwjmdwdpsfwfspjgtmfcvddgspldbldtbtwrzdsjrbhvvcjgnrsbzvbrnqjwhrzgfsbdjlfqlszvlnrbfcrgfwrsmqmmnrwbtvfdpjzpfbhplfdsrwwgqqtgnzvddbgjjllmmcjjlglwmsbwrdrnnznwzplnbhlrlnmnllwgwgdpqdqqlmvsbgcshsmntrrlrvdhjgctzsfhmvfqtthvvchftflhlqqhhhbhqvgwtcmgcfwldhgptfddpsqrfzqmtpszswfrztzfsspltcvjwwsljsnjpnnqggscwwmcwfrljlrtqwqvplthsctvbndjfpnvcbdngzqtgjvwlsdhthdwmjvtnzrplwzwsfmgszpqjcjttslsmtbbvhjgpqmqfjbcccsnrlwmjhbsqgzqldmlhnbjnjfwmgzpvdcwndbwcncmtzccngcghhpwmjnncfgqtdtzwmhbdrpwsfbnjzfnwzwqncnlfjqjrjhgnqgvbcdhgdnbwpqjcfgprmfhzlrqtwlqpshfrgdszrwdtqfcntrzbgzlvrhtlsbjjwtnlqllnsvbzwjlmqvdgvtslmbwwcfstmqntwwwsjmrflrqnttfzjchpgwczzdtqbhdrtrpvhhbscvjtdtrhbstpqrnrzszwvcqzhbrzhlblvzrgwtqzbslbmgdqhpfqrdqrzcsbglcsshcwvlcpgjtjmcgpmsnldjzlwnrqlzzznpvmgssvzshjvtsmmzvstpqrhfvttnsrddfcqcbwhgpfdtlhcvcgjgdrvvntvdjqpvwvfmphhpzjgmshddqfsbpjbzrfdjnwrhmgcfbccmzqgvrbmcjdpvwfrtdpbwvjtjcrmnpzrrqbbvbsgcplwmlbsdwptbprlczjcqhdzprpttvnthbmtscdtjvrnwqhnvqbzvwnphnzwlgvvjhddjvjrvwlmhqcsffcnhgjzdjppqqwbglbhgzsmvzwjdvbqpztphshtrbrrhzmdlfdtssbhrcltwlqpzvpgbsgngpfjsjbrnnlzctqcqzwswhfnjjngwsztdgmmcffqfhbsgwstnflqjqttzbtgjvcfrrdwzcvhwjnhmtphszrsptjsqqwcwfnmtlzvzsqsmghtztrpvdslrmjqqvwfmzlwwjbwtpmhtqcfctdztsnfrhfqwqcjdzmjhvwwgrslmdqqwgwfvwlzzsznmdrzgcvbmrtcvjsqlftnpdhwmrzjwsnjjdrczbjcwhwlrtljwjsfmcfcrsjflsldbjrzpdgltmhtszzznjjlfqmgpbjfjncvtvlcfsmltbsvsrgdhwwhcpbdbntqhgjztvlwtwdsgqfwtlcdzffcszjmjvj"