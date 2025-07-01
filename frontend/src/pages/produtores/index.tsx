import React, { useEffect } from 'react';
import Link from 'next/link';
import Layout from '@/components/Layout/Layout';
import styled from 'styled-components';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '@/store';
import { fetchProdutores, deleteProdutor } from '@/store/produtoresSlice';
import toast from 'react-hot-toast';
import Head from 'next/head';

const Container = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.08);
`;

const Title = styled.h1`
  color: #333;
  margin-bottom: 2rem;
`;

const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 2rem;
`;

const Th = styled.th`
  background: #f5f5f5;
  color: #333;
  padding: 0.75rem;
  text-align: left;
`;

const Td = styled.td`
  padding: 0.75rem;
  border-bottom: 1px solid #eee;
`;

const Actions = styled.div`
  display: flex;
  gap: 0.5rem;
`;

const ActionButton = styled.button`
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.4rem 0.8rem;
  font-size: 0.95rem;
  cursor: pointer;
  transition: background 0.2s;
  &:hover { background: #388e3c; }
`;

const NewButton = styled(Link)`
  display: inline-block;
  background: #2196f3;
  color: white;
  padding: 0.7rem 1.2rem;
  border-radius: 4px;
  text-decoration: none;
  margin-bottom: 1.5rem;
  font-weight: 500;
  &:hover { background: #1976d2; }
`;

const Loading = styled.div`
  text-align: center;
  color: #888;
  padding: 2rem;
`;

const Error = styled.div`
  text-align: center;
  color: #d32f2f;
  background: #ffebee;
  border-radius: 8px;
  margin: 1rem 0;
  padding: 1rem;
`;

const ProdutoresPage: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { produtores, loading, error } = useSelector((state: RootState) => state.produtores);

  useEffect(() => {
    dispatch(fetchProdutores());
  }, [dispatch]);

  const handleDelete = async (id: number) => {
    if (window.confirm('Tem certeza que deseja excluir este produtor? Essa ação não pode ser desfeita.')) {
      try {
        await dispatch(deleteProdutor(id)).unwrap();
        toast.success('Produtor excluído com sucesso!');
      } catch (err: any) {
        toast.error(err?.message || 'Erro ao excluir produtor');
      }
    }
  };

  return (
    <Layout>
      <Head>
        <title>Produtores Rurais | Brain Agriculture</title>
      </Head>
      <Container>
        <Title>Produtores Rurais</Title>
        <NewButton href="/produtores/novo">+ Novo Produtor</NewButton>
        {loading ? (
          <Loading>Carregando produtores...</Loading>
        ) : error ? (
          <Error>Erro ao carregar produtores: {error}</Error>
        ) : (
          <Table>
            <thead>
              <tr>
                <Th>Nome</Th>
                <Th>CPF/CNPJ</Th>
                <Th>Fazendas</Th>
                <Th>Ações</Th>
              </tr>
            </thead>
            <tbody>
              {produtores.length === 0 ? (
                <tr>
                  <Td colSpan={4} style={{ textAlign: 'center', color: '#888' }}>
                    Nenhum produtor cadastrado.
                  </Td>
                </tr>
              ) : (
                produtores.map((produtor) => (
                  <tr key={produtor.id}>
                    <Td>{produtor.nome}</Td>
                    <Td>{produtor.cpf_cnpj}</Td>
                    <Td>{produtor.fazendas?.length || 0}</Td>
                    <Td>
                      <Actions>
                        <Link href={`/produtores/${produtor.id}`} passHref>
                          <ActionButton as="a">Visualizar</ActionButton>
                        </Link>
                        <Link href={`/produtores/${produtor.id}/editar`} passHref>
                          <ActionButton as="a" style={{ background: '#ff9800' }}>Editar</ActionButton>
                        </Link>
                        <ActionButton style={{ background: '#f44336' }} onClick={() => handleDelete(produtor.id)}>
                          Excluir
                        </ActionButton>
                      </Actions>
                    </Td>
                  </tr>
                ))
              )}
            </tbody>
          </Table>
        )}
      </Container>
    </Layout>
  );
};

export default ProdutoresPage; 