import React, { useEffect } from 'react';
import { useRouter } from 'next/router';
import Layout from '@/components/Layout/Layout';
import styled from 'styled-components';
import Link from 'next/link';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '@/store';
import { fetchProdutor } from '@/store/produtoresSlice';

const Container = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.08);
`;

const Title = styled.h1`
  color: #333;
  margin-bottom: 1.5rem;
`;

const Section = styled.section`
  margin-bottom: 2rem;
`;

const Label = styled.span`
  font-weight: 500;
  color: #555;
`;

const Value = styled.span`
  color: #222;
  margin-left: 0.5rem;
`;

const Actions = styled.div`
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
`;

const ActionButton = styled.button`
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1.2rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
  &:hover { background: #388e3c; }
`;

const FazendaCard = styled.div`
  background: #f9f9f9;
  border-radius: 6px;
  padding: 1rem;
  margin-bottom: 1rem;
`;

const CulturaList = styled.ul`
  margin: 0.5rem 0 0 1rem;
  padding: 0;
`;

const CulturaItem = styled.li`
  color: #333;
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

const ProdutorDetailPage: React.FC = () => {
  const router = useRouter();
  const { id } = router.query;
  const dispatch = useDispatch<AppDispatch>();
  const { selectedProdutor: produtor, loading, error } = useSelector((state: RootState) => state.produtores);

  useEffect(() => {
    if (id && typeof id === 'string') {
      dispatch(fetchProdutor(Number(id)));
    }
  }, [dispatch, id]);

  return (
    <Layout>
      <Container>
        <Title>Detalhes do Produtor</Title>
        {loading ? (
          <Loading>Carregando produtor...</Loading>
        ) : error ? (
          <Error>Erro ao carregar produtor: {error}</Error>
        ) : !produtor ? (
          <Error>Produtor não encontrado.</Error>
        ) : (
          <>
            <Actions>
              <Link href={`/produtores/${produtor.id}/editar`} passHref>
                <ActionButton as="a" style={{ background: '#ff9800' }}>Editar</ActionButton>
              </Link>
            </Actions>
            <Section>
              <Label>Nome:</Label> <Value>{produtor.nome}</Value><br />
              <Label>CPF/CNPJ:</Label> <Value>{produtor.cpf_cnpj}</Value><br />
              <Label>Data de Cadastro:</Label> <Value>{produtor.created_at ? new Date(produtor.created_at).toLocaleString('pt-BR') : '-'}</Value>
            </Section>
            <Section>
              <h2>Fazendas</h2>
              {produtor.fazendas?.length ? (
                produtor.fazendas.map((fazenda) => (
                  <FazendaCard key={fazenda.id}>
                    <div><Label>Nome:</Label> <Value>{fazenda.nome}</Value></div>
                    <div><Label>Cidade:</Label> <Value>{fazenda.cidade}</Value></div>
                    <div><Label>Estado:</Label> <Value>{fazenda.estado}</Value></div>
                    <div><Label>Área Total:</Label> <Value>{fazenda.area_total} ha</Value></div>
                    <div><Label>Área Agricultável:</Label> <Value>{fazenda.area_agricultavel} ha</Value></div>
                    <div><Label>Área de Vegetação:</Label> <Value>{fazenda.area_vegetacao} ha</Value></div>
                    <div>
                      <Label>Culturas:</Label>
                      <CulturaList>
                        {fazenda.culturas?.length ? (
                          fazenda.culturas.map((cultura) => (
                            <CulturaItem key={cultura.id}>
                              {cultura.nome} ({cultura.safra})
                              {/* Botão de excluir cultura pode ser implementado aqui */}
                            </CulturaItem>
                          ))
                        ) : (
                          <CulturaItem>Nenhuma cultura cadastrada.</CulturaItem>
                        )}
                      </CulturaList>
                    </div>
                  </FazendaCard>
                ))
              ) : (
                <div style={{ color: '#888' }}>Nenhuma fazenda cadastrada.</div>
              )}
            </Section>
          </>
        )}
      </Container>
    </Layout>
  );
};

export default ProdutorDetailPage; 