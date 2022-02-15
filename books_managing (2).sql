PGDMP
     *    
        
        z            books_managing    11.14    11.14                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                       1262    16503    books_managing    DATABASE     �   CREATE DATABASE books_managing WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'French_France.1252' LC_CTYPE = 'French_France.1252';
    DROP DATABASE books_managing;
             postgres    false            �            1259    16506 
   categories    TABLE     n   CREATE TABLE public.categories (
    id_categorie integer NOT NULL,
    libelle character varying NOT NULL
);
    DROP TABLE public.categories;
       public         postgres    false            �            1259    16504    categories_id_categorie_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_id_categorie_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.categories_id_categorie_seq;
       public       postgres    false    197                       0    0    categories_id_categorie_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.categories_id_categorie_seq OWNED BY public.categories.id_categorie;
            public       postgres    false    196            �            1259    16517    livres    TABLE       CREATE TABLE public.livres (
    id_livre integer NOT NULL,
    isbn character varying(30) NOT NULL,
    titre character varying(80) NOT NULL,
    date_publication date NOT NULL,
    auteur character varying NOT NULL,
    editeur character varying NOT NULL,
    id_categorie integer
);
    DROP TABLE public.livres;
       public         postgres    false            �            1259    16515    livres_id_livre_seq    SEQUENCE     �   CREATE SEQUENCE public.livres_id_livre_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.livres_id_livre_seq;
       public       postgres    false    199                       0    0    livres_id_livre_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.livres_id_livre_seq OWNED BY public.livres.id_livre;
            public       postgres    false    198            �
           2604    16509    categories id_categorie    DEFAULT     �   ALTER TABLE ONLY public.categories ALTER COLUMN id_categorie SET DEFAULT nextval('public.categories_id_categorie_seq'::regclass);
 F   ALTER TABLE public.categories ALTER COLUMN id_categorie DROP DEFAULT;
       public       postgres    false    196    197    197            �
           2604    16520    livres id_livre    DEFAULT     r   ALTER TABLE ONLY public.livres ALTER COLUMN id_livre SET DEFAULT nextval('public.livres_id_livre_seq'::regclass);
 >   ALTER TABLE public.livres ALTER COLUMN id_livre DROP DEFAULT;
       public       postgres    false    198    199    199            
          0    16506 
   categories 
   TABLE DATA               ;   COPY public.categories (id_categorie, libelle) FROM stdin;
    public       postgres    false    197   �                 0    16517    livres 
   TABLE DATA               h   COPY public.livres (id_livre, isbn, titre, date_publication, auteur, editeur, id_categorie) FROM stdin;
    public       postgres    false    199   d                  0    0    categories_id_categorie_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.categories_id_categorie_seq', 23, true);
            public       postgres    false    196                       0    0    livres_id_livre_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.livres_id_livre_seq', 48, true);
            public       postgres    false    198            �
           2606    16514    categories categories_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id_categorie);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public         postgres    false    197            �
           2606    16527    livres livres_isbn_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_isbn_key UNIQUE (isbn);
 @   ALTER TABLE ONLY public.livres DROP CONSTRAINT livres_isbn_key;
       public         postgres    false    199            �
           2606    16525    livres livres_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_pkey PRIMARY KEY (id_livre);
 <   ALTER TABLE ONLY public.livres DROP CONSTRAINT livres_pkey;
       public         postgres    false    199            �
           2606    16529    livres livres_titre_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_titre_key UNIQUE (titre);
 A   ALTER TABLE ONLY public.livres DROP CONSTRAINT livres_titre_key;
       public         postgres    false    199            �
           2606    16530    livres livres_id_categorie_fkey 
   FK CONSTRAINT     �   ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_id_categorie_fkey FOREIGN KEY (id_categorie) REFERENCES public.categories(id_categorie);
 I   ALTER TABLE ONLY public.livres DROP CONSTRAINT livres_id_categorie_fkey;
       public       postgres    false    197    2696    199            
   U  x�UQ�N1�g��U��&)�Q BIc9C2��^<v$~�n�c�q��(\��y�p����g%C�x���;����-��'�G�s����V�x����z���%�H�až����OLpqW~���hg}��g�K�q,Mz�|md�Wp_��ٕ�Lp	,%)%�3x�}������r���H8ʑ
���Fu��9<s)Өt�1,��FT���:<���3噑*E��)��!�h/����Ʀ(g.�VB���Qh��^�geT��_S�����(M���-��]�N
-4��`����SG򅝅͐��B���1��_:�u���4��4���!}��zx?E�!��         �
  x�eXKs�>��{ٹ��s��c�=�خ�l*��D��Ie4���ܲN�Bn�c�$e��jjJ%������P�ʼ�#?���O�$�3�`6{.{�ʎ��F~��TK~/��XD�D~�;U5�m%��ݳ�V;<zx�U���X�E.A�q��y�~�����Y��FU�Щ����i%�NxXf�ߛZ�6,��Bv#u��$��It8�F�x*�(J�e1J�=�-lM��Y�JQ��b?,�/����םUg4�� to)�"%a�i��~�n%�*�
���)�(=�(u+,��,��Ա�C����e-�'���]��Vh%���b�٥�]�|�<� 
p�0�ʷ1���])M}�a��K�ۢ���P���H�}L��7BWf�P깰kJy��;��1��=�,��J�r���1G�Qξ�F*��X�l�F�/�7hR���iS:m^ 21;=�W�����sF1���)t�A��_�P̃���/���Wa�ޜ��`�b`D4��݉N ?�����`@S�r�Z�%~������AuJ��|�0'QUf�k}x�b'+�4��1��İ�'~7�#���=������j�v+�E�i.%�h�J��,�0�� A���x��!�U }wB��$>!|����[��X�����R)������� ���Cԃ ��њZ���#,O4}2�t���9�t	@n/Cש��G��|��PQ�3t�Jj�Ts뮯�Rt\����
)'�D{vzx�;k:;�����
k�E�9�#@0�8���̘��	�5�O���������0zE��PY�޾�R�J��~e�܁�N�V�D-zǯ�Y�,��K3�t��-LҲ,��ıvyx���F�=�l��HؠD�������ӯ�)z�1%,Q��~�Ѡ�h��C`3^�h�z�K�9�Qe4���\v�A(/K��U�
1�����lI� '�mC>��ЃNN�ģX@���S&ٞ��]c�-T%��Wu(s?��p/�JV$��dw$�s��˷4�Uh�_��["���$\ð�g���$�34	x�JS���'ȔV߅������� �f�P�����b'T˕�
�v	Sg
9��7����܊��ع=Ҹ3�F&�4�G�%}h�n#O�<����od���跆�Vx�N*gBg�˽�<V�S�K�'�:��p��{kP��4���("j%��.��
�z���|�W��BKY�E�ѳ!�'ünѯU�U����L�x�����AZ;�
�f��C��Q�V�
����D��b耖�^s��"I	+`=[�US!�HL�[��B�m�@���h(�e=����H�@��J��O�� �J���^Aˌ�-9,z��U�7{(G��W�~B&F��������P˕*�E�.�-�E��f��yf����@	�9?&t�ݝ��`�f)���#�����ك��,�TR�y�

��L_KHJ�ͺ�~o"��᷁���-0�hV�8"����jT��Mޚ5L���E�&@A��t82R~�M
���%K��e�u�B��oTD1�d��_���i�9�(�^��ކ�p�7.?�w���q�;��[�Cv.u�n�JB��ՠj��o@��=lA��kh�ղ�p����O���j�J4�F5>(�^;��F����
�o��;C*�AY��D}P��>�<�� � #�J��^w������d��`�%��+츜�9�$��uF
%�ӄ@Sg0r�,�>���/���m͢���ܶF��ђ�!e<�B�$���Q�~ճ�:x�7�Σ�ƨ<?~t�o4Z���(���E���#����B���ʾ3�7�"����J<¥O.m%'�Ƴ����é�B~a&_E߈1�
IP@�J1�C� pM���	�N��LO�3�g�����
v���ō��-Ľ��`�dD>�tg*�
�jF=$'�-v�Ѡ�{��bʚҞ�E�Ko��C�K�XM�}IN7��vZ��je�d��E�ϡC��������T���R�S؊�A.N���� {y�~&I��ж�"�Y��[K��s��b)��GD��e.��xV� ��y!c�:3&��R	����Y�K��%�KAm���8�6�6���EHf���}v�I3��S
�bݟ���:��-���+��{<��޳0��#��8Dd,|pF�/ɥgS�t���ݪg��K�|�vV���s�0���A���c���J�����^��a�2-�m� �5�Hfb�1F�
4r~�@6% `8�	Jvk�U�1�-*���a���b�4�u77����XZ ��Mן/a��� ��e%̼$:n�E	����u�
�vJ*/���߹��������R;��,܋��q�yP;p�ν$~�Y��>�uP�^�k�k@7����NP�/j˟=|狅�$��"R,$1{����5��P��!��;\i_@9ݸ��˚�=��j�[�,���aՃs�Y�J/9n�Y�� qF���(*�ݟv����I�	yB2�]��i�N�万��4����G]v=����W�FV�a:써̒/�Z�~j���ZzI�~ E0�������0�HQ�;��v7uz���KFr����k�(�����߷�E�ٵ'tÐ��#_|�v)�߅>��X��c����}���>z��ǌ�     